from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status

from app.core.config import get_settings
from app.core.security import create_access_token, hash_password, require_dashboard_user, verify_password
from app.db.mongodb import get_db
from app.schemas.auth import (
    CurrentUserResponse,
    ForgotPasswordRequest,
    LoginChallengeResponse,
    LoginRequest,
    ResetPasswordRequest,
    TokenResponse,
    VerifyLoginRequest,
)
from app.services.auth_service import create_code_challenge, hash_code, send_email, utc_now

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=LoginChallengeResponse)
async def login(payload: LoginRequest):
    email = str(payload.email).lower()
    user = await get_db().users.find_one({"_id": email, "active": True})
    if user is None or not verify_password(payload.password, user.get("password_hash", "")):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    challenge_id, code = await create_code_challenge(email, "login")
    email_sent = True
    try:
        await send_email("masabimiskat@gmail.com", "Your Blacksoft dashboard verification code", f"Your verification code is {code}. It expires soon.")
    except Exception as exc:
        email_sent = False
        print(f"Failed to send verification email: {exc}")

    return LoginChallengeResponse(
        challenge_id=challenge_id,
        expires_in=get_settings().verification_code_minutes * 60,
        code=code if not email_sent else None
    )


@router.post("/verify-login", response_model=TokenResponse)
async def verify_login(payload: VerifyLoginRequest):
    settings = get_settings()
    challenges = get_db().auth_challenges
    challenge = await challenges.find_one({"_id": payload.challenge_id, "purpose": "login"})
    if challenge is None or challenge["expires_at"] <= utc_now() or challenge.get("attempts", 0) >= settings.max_code_attempts:
        raise HTTPException(status_code=400, detail="Invalid or expired verification code")
    if challenge.get("code_hash") != hash_code(payload.code):
        await challenges.update_one({"_id": payload.challenge_id}, {"$inc": {"attempts": 1}})
        raise HTTPException(status_code=400, detail="Invalid or expired verification code")

    await challenges.delete_one({"_id": payload.challenge_id})
    user = await get_db().users.find_one({"_id": challenge["email"], "active": True})
    if user is None:
        raise HTTPException(status_code=401, detail="User is not active")
    token, expires_in = create_access_token(challenge["email"], user.get("role", "admin"))
    return TokenResponse(access_token=token, expires_in=expires_in)


@router.post("/forgot-password", status_code=status.HTTP_202_ACCEPTED)
async def forgot_password(payload: ForgotPasswordRequest):
    email = str(payload.email).lower()
    user = await get_db().users.find_one({"_id": email, "active": True})
    if user is not None:
        try:
            _, code = await create_code_challenge(email, "password_reset")
            await send_email(email, "Reset your Blacksoft dashboard password", f"Your password reset code is {code}. It expires soon.")
        except Exception:
            pass
    return {"message": "If the account exists, a reset code has been sent."}


@router.post("/reset-password")
async def reset_password(payload: ResetPasswordRequest):
    settings = get_settings()
    email = str(payload.email).lower()
    challenges = get_db().auth_challenges
    challenge = await challenges.find_one({"email": email, "purpose": "password_reset"})
    if challenge is None or challenge["expires_at"] <= utc_now() or challenge.get("attempts", 0) >= settings.max_code_attempts:
        raise HTTPException(status_code=400, detail="Invalid or expired reset code")
    if challenge.get("code_hash") != hash_code(payload.code):
        await challenges.update_one({"_id": challenge["_id"]}, {"$inc": {"attempts": 1}})
        raise HTTPException(status_code=400, detail="Invalid or expired reset code")

    await get_db().users.update_one({"_id": email}, {"$set": {"password_hash": hash_password(payload.new_password)}})
    await challenges.delete_one({"_id": challenge["_id"]})
    return {"message": "Password reset successfully"}


@router.get("/me", response_model=CurrentUserResponse)
async def current_user(user: dict = Depends(require_dashboard_user)):
    return user
