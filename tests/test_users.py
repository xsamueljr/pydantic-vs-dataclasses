from uuid import uuid4

import pytest
from pydantic import ValidationError

from src.dataclass_user import User as DUser
from src.pydantic_user import User as PUser


@pytest.fixture
def password() -> str:
    """Crea aleatoriamente una contraseña válida"""
    return "".join((str(uuid4())[:12], "a1A!"))


VALID_EMAILS = (
    "test@gmail.com",
    "example@example.com",
    "pedromecanico@yahoo.es",
    "1234@hotmail.com"
)

INVALID_EMAILS = (
    "nonono",
    "no tengo correo",
    "mi casa",
    "berenjenas",
    "claro@claro",
    "oscuro@oscuro."
)

INVALID_PASSWORDS = (
    "123456789ABCDE",
    "contraseña",
    "pipipupu2354ñpsv!", # Longitud: 17
    "1A!aa!A1", # Palíndromo
    "aS!4hfywe ", # Espacios al final
    " aS!4hfywe", # Espacios al principio
    " aS!4hfywe ", # Espacios en ambos lados
    "aS!4 hfywe" # Espacio en medio
)


@pytest.mark.parametrize("email", VALID_EMAILS)
def test_can_create_users_with_valid_email(password, email):
    user1 = DUser(email=email, password=password)
    user2 = PUser(email=email, password=password)

    for i in (user1, user2):
        assert i.email == email
        assert i.password == password


@pytest.mark.parametrize("email", INVALID_EMAILS)
def test_cannot_create_users_with_invalid_email(password, email):
    with pytest.raises(ValueError):
        _ = DUser(email=email, password=password)

    with pytest.raises(ValidationError):
        _ = PUser(email=email, password=password)


@pytest.mark.parametrize("invalid_password", INVALID_PASSWORDS)
def test_cannot_create_users_with_invalid_password(invalid_password):
    with pytest.raises(ValueError):
        _ = DUser(email="test@example.com", password=invalid_password)

    with pytest.raises(ValueError):
        _ = PUser(email="test@example.com", password=invalid_password)
