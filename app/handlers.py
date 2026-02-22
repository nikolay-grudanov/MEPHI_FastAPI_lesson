"""Эндпоинты API для FastAPI приложения."""

from fastapi import APIRouter, Body, HTTPException

from forms import UserNameParts, BirthDate

from query import getIp, getTime, getHoroscope, getZodiacSign

router = APIRouter()


@router.get("/")
async def index() -> dict[str, str]:
    """Корневой эндпоинт для проверки работы сервера."""
    return {"status": "Ok"}


@router.get("/users/{username}", name="Hello user")
async def read_user(username: str) -> dict[str, str]:
    """Возвращает приветствие для пользователя.

    Args:
        username: Имя пользователя из пути

    Returns:
        Словарь с сообщением приветствия
    """
    return {"message": f"Hello {username}"}


@router.post("/users/full-name", name="Full name")
async def full_name(user_from: UserNameParts = Body(..., embed=True)) -> dict[str, str]:
    """Возвращает полное имя из частей.

    Args:
        user_from: Модель с частями имени

    Returns:
        Словарь с полным именем
    """
    return {
        "fullName": f"{user_from.lastName.strip()} {user_from.firstName.strip()} {user_from.middleName.strip()}"
    }


@router.get("/users/current/ip", name="Получить текущий ip")
async def current_ip() -> str:
    """Возвращает текущий IP-адрес клиента.

    Returns:
        Строка с IP-адресом
    """
    ip = getIp()
    return ip


@router.get("/users/current/full-time", name="Получить текущее время")
async def current_full_time() -> dict:
    """Получает текущее время по IP-адресу.

    Returns:
        Словарь с информацией о времени
    """
    ip = getIp()
    full_time = getTime(ip)
    return full_time


@router.post("/horoscope", name="Получить гороскоп")
async def horoscope(birth_data: BirthDate) -> dict[str, str]:
    """Возвращает знак зодиака и гороскоп по дате рождения.

    Args:
        birth_data: Модель с датой рождения

    Returns:
        Словарь с знаком зодиака и гороскопом
    """
    try:
        day = birth_data.birthDate.day
        month = birth_data.birthDate.month
        sign = getZodiacSign(day, month)
        horoscope_data = getHoroscope(sign)
        return {
            "sign": sign,
            "horoscope": horoscope_data.get("horoscope", "Нет данных"),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка: {str(e)}")
