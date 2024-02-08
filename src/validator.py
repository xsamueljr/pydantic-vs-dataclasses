"""Módulo para encapsular toda la lógica de validación por separado, en la clase `Guard`."""
from re import match


EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

NUMBERS = "0123456789"
LETTERS = "abcdefghijklmnñopqrstuvwxyz"
CAPITAL_LETTERS = LETTERS.upper()
SPECIAL_CHARACTERS = r"\/()@ºª`ç,;*!.¡¿?/#%&"
ALL: tuple[str, ...] = (SPECIAL_CHARACTERS, CAPITAL_LETTERS, NUMBERS, LETTERS)


class Guard:
    @staticmethod
    def against_email(email: str) -> None:
        """El email es válido

        (Ésta guardia está pensada para `dataclasses`, en Pydantic lo suyo es usar `EmailStr`)"""
        if not match(EMAIL_REGEX, email):
            raise ValueError("La dirección de correo no es válida")

    @staticmethod
    def against_whitespaces(password: str) -> None:
        """La contraseña no tiene espacios."""
        if " " in password:
            raise ValueError("La contraseña no puede tener espacios")

    @staticmethod
    def against_length(password: str) -> None:
        """La longitud de la contraseña es válida"""
        length = len(password)
        if length < 8 or length > 16:
            raise ValueError("La contraseña debe tener un mínimo de 8 caracteres y un máximo de 16")

    @staticmethod
    def against_variety(password: str) -> None:
        """La contraseña tiene mínimo 1 número, 1 letra mayúscula, una minúscula y un caracter especial"""
        for chars in ALL:
            counter = sum(password.count(char) for char in chars)

            if counter < 1:
                raise ValueError("La contraseña debe tener mínimo 1 número, una mayúscula, una minúscula y un caracter especial")

    @staticmethod
    def against_palindrome(password: str) -> None:
        """La contraseña no es un palíndromo

        (No se lee igual al darle la vuelta)"""
        if password == password[::-1]:
            raise ValueError("La contraseña no puede ser un palíndromo")
