from __future__ import annotations

import asyncio
import hashlib
import secrets
import smtplib
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage

from app.core.config import get_settings
from app.core.security import hash_password
from app.db.mongodb import get_db


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def hash_code(code: str) -> str:
    return hashlib.sha256(code.encode("utf-8")).hexdigest()


def generate_code() -> str:
    return f"{secrets.randbelow(1_000_000):06d}"


def smtp_is_configured() -> bool:
    settings = get_settings()
    return all([settings.smtp_host, settings.smtp_username, settings.smtp_password, settings.smtp_from])


def validate_auth_settings() -> None:
    settings = get_settings()
    if settings.app_env.lower() == "production":
        if not settings.admin_email or not settings.admin_password:
            raise RuntimeError("ADMIN_EMAIL and ADMIN_PASSWORD must be configured in production")
        if settings.jwt_secret == "change-this-in-production" or len(settings.jwt_secret) < 32:
            raise RuntimeError("JWT_SECRET must be a long random value in production")
        if not smtp_is_configured():
            raise RuntimeError("SMTP settings must be configured in production")


def _send_email_sync(to_email: str, subject: str, body: str) -> None:
    settings = get_settings()
    if not smtp_is_configured():
        raise RuntimeError("SMTP is not configured")

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = settings.smtp_from
    message["To"] = to_email
    message.set_content(body)

    with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=20) as server:
        if settings.smtp_use_tls:
            server.starttls()
        server.login(settings.smtp_username, settings.smtp_password)
        server.send_message(message)


async def send_email(to_email: str, subject: str, body: str) -> None:
    await asyncio.to_thread(_send_email_sync, to_email, subject, body)


async def create_admin_user() -> None:
    settings = get_settings()
    if not settings.admin_email or not settings.admin_password:
        return

    email = settings.admin_email.strip().lower()
    users = get_db().users
    existing = await users.find_one({"_id": email})
    if existing is None:
        await users.insert_one({
            "_id": email,
            "email": email,
            "password_hash": hash_password(settings.admin_password),
            "role": "admin",
            "active": True,
            "created_at": utc_now(),
        })


async def create_code_challenge(email: str, purpose: str) -> tuple[str, str]:
    settings = get_settings()
    code = generate_code()
    challenge_id = secrets.token_urlsafe(32)
    await get_db().auth_challenges.delete_many({"email": email, "purpose": purpose})
    await get_db().auth_challenges.insert_one({
        "_id": challenge_id,
        "email": email,
        "purpose": purpose,
        "code_hash": hash_code(code),
        "expires_at": utc_now() + timedelta(minutes=settings.verification_code_minutes),
        "attempts": 0,
    })
    return challenge_id, code
