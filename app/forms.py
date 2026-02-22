"""Pydantic-модели для валидации данных."""

from pydantic import BaseModel
from datetime import date


class UserNameParts(BaseModel):
    """Модель для валидации частей имени пользователя."""

    lastName: str
    firstName: str
    middleName: str


class BirthDate(BaseModel):
    """Модель для валидации даты рождения."""

    birthDate: date
