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

    ЗАДАНИЕ СТУДЕНТА: Реализуйте эту функцию используя
    API сервиса https://www.timeapi.io/swagger/index.html

    Подсказки:
    1. Используйте эндпоинт Time/current/ip?ipAddress={ip}
    2. Отправьте GET запрос с заголовком accept: application/json
    3. Верните результат response.json()

    Args:
        ip (str): IP-адрес

    Returns:
        Dict[str, str]: Словарь с информацией о времени

    Raises:
        NotImplementedError: Функция еще не реализована студентом
    """
    raise NotImplementedError(
        "Студенту необходимо реализовать эту функцию. См. документацию в docstring"
    )


def getHoroscope(sign: str) -> Dict[str, str]:
    """Получает гороскоп для знака зодиака.

    ЗАДАНИЕ СТУДЕНТА: Реализуйте эту функцию используя
    API сервиса https://www.ohmanda.com/api/horoscope/

    Подсказки:
    1. Используйте эндпоинт /api/horoscope/today?sign={sign}
    2. sign должен быть на английском (например, 'aries', 'taurus')
    3. Отправьте GET запрос
    4. Верните результат response.json()

    Args:
        sign (str): Знак зодиака на английском (например, 'aries')

    Returns:
        Dict[str, str]: Словарь с гороскопом

    Raises:
        NotImplementedError: Функция еще не реализована студентом
    """
    raise NotImplementedError(
        "Студенту необходимо реализовать эту функцию. См. документацию в docstring"
    )


def getZodiacSign(day: int, month: int) -> str:
    """Определяет знак зодиака по дате рождения.

    ЗАДАНИЕ СТУДЕНТА: Реализуйте эту функцию для определения знака зодиака.

    Подсказки:
    1. Знак зодиака определяется по дате рождения (день и месяц)
    2. Границы знаков:
       - Овен (aries): 21 марта - 19 апреля
       - Телец (taurus): 20 апреля - 20 мая
       - Близнецы (gemini): 21 мая - 20 июня
       - Рак (cancer): 21 июня - 22 июля
       - Лев (leo): 23 июля - 22 августа
       - Дева (virgo): 23 августа - 22 сентября
       - Весы (libra): 23 сентября - 22 октября
       - Скорпион (scorpio): 23 октября - 21 ноября
       - Стрелец (sagittarius): 22 ноября - 21 декабря
       - Козерог (capricorn): 22 декабря - 19 января
       - Водолей (aquarius): 20 января - 18 февраля
       - Рыбы (pisces): 19 февраля - 20 марта
    3. Верните название знака на английском языке

    Args:
        day (int): День рождения
        month (int): Месяц рождения

    Returns:
        str: Знак зодиака на английском

    Raises:
        NotImplementedError: Функция еще не реализована студентом
    """
    raise NotImplementedError(
        "Студенту необходимо реализовать эту функцию. См. документацию в docstring"
    )
