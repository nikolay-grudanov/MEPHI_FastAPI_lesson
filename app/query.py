"""Модуль для работы с внешними API и запросов."""

import requests
from typing import Dict


def getIp() -> str:
    """Получает текущий IP-адрес.

    Returns:
        str: IP-адрес в формате строки
    """
    url = "https://ifconfig.me/ip"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text.strip()


def getTime(ip: str) -> Dict[str, str]:
    """Получает текущее время по IP-адресу.

    Args:
        ip (str): IP-адрес

    Returns:
        Dict[str, str]: Словарь с информацией о времени
    """
    url = f"https://www.timeapi.io/api/Time/current/ip?ipAddress={ip}"
    payload = {}
    headers = {"accept": "application/json"}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def getHoroscope(sign: str) -> Dict[str, str]:
    """Получает гороскоп для знака зодиака.

    Args:
        sign (str): Знак зодиака на английском (например, 'aries')

    Returns:
        Dict[str, str]: Словарь с гороскопом
    """
    url = f"https://www.ohmanda.com/api/horoscope/today?sign={sign}"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def getZodiacSign(day: int, month: int) -> str:
    """Определяет знак зодиака по дате рождения.

    Args:
        day (int): День рождения
        month (int): Месяц рождения

    Returns:
        str: Знак зодиака на английском
    """
    # Знаки зодиака и их периоды
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "aries"  # Овен
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "taurus"  # Телец
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "gemini"  # Близнецы
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "cancer"  # Рак
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "leo"  # Лев
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "virgo"  # Дева
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "libra"  # Весы
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "scorpio"  # Скорпион
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "sagittarius"  # Стрелец
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "capricorn"  # Козерог
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "aquarius"  # Водолей
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "pisces"  # Рыбы
    else:
        raise ValueError("Некорректная дата")
