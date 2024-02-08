from pydantic import BaseModel, EmailStr, field_validator
from .validator import Guard


class User(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value: str):
        Guard.against_whitespaces(value)
        Guard.against_length(value)
        Guard.against_palindrome(value)
        Guard.against_variety(value)

        return value
