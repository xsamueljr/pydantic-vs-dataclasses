from dataclasses import dataclass
from .validator import Guard


@dataclass
class User:
    email: str
    password: str

    def __post_init__(self):
        Guard.against_email(self.email)
        Guard.against_whitespaces(self.password)
        Guard.against_length(self.password)
        Guard.against_palindrome(self.password)
        Guard.against_variety(self.password)
