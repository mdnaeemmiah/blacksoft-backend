from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class LoginChallengeResponse(BaseModel):
    challenge_id: str
    expires_in: int


class VerifyLoginRequest(BaseModel):
    challenge_id: str = Field(min_length=1, max_length=100)
    code: str = Field(pattern=r"^\d{6}$")


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    email: EmailStr
    code: str = Field(pattern=r"^\d{6}$")
    new_password: str = Field(min_length=8, max_length=128)


class CurrentUserResponse(BaseModel):
    email: EmailStr
    role: str
