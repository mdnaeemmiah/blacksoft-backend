from pydantic import BaseModel, Field, field_validator


def _normalize_email(value: str) -> str:
    email = value.strip().lower()
    if "@" not in email or email.count("@") != 1:
        raise ValueError("value is not a valid email address")

    local_part, domain_part = email.split("@", 1)
    if not local_part or not domain_part:
        raise ValueError("value is not a valid email address")
    if local_part.startswith(".") or local_part.endswith(".") or ".." in local_part:
        raise ValueError("value is not a valid email address")
    if domain_part.startswith(".") or domain_part.endswith(".") or ".." in domain_part:
        raise ValueError("value is not a valid email address")

    return email


class EmailModel(BaseModel):
    email: str = Field(min_length=3, max_length=320)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        return _normalize_email(value)


class LoginRequest(EmailModel):
    password: str = Field(max_length=128)


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


class ForgotPasswordRequest(EmailModel):
    pass


class ResetPasswordRequest(EmailModel):
    code: str = Field(pattern=r"^\d{6}$")
    new_password: str = Field(min_length=8, max_length=128)


class CurrentUserResponse(EmailModel):
    role: str
