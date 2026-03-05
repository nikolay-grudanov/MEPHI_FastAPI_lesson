#!/bin/bash

# Скрипт для быстрой настройки uv окружения в учебном проекте FastAPI
# MEPHI FastAPI Lesson - Установка uv и настройка проекта

set -e  # Остановить выполнение при любой ошибке

echo "=========================================="
echo "MEPHI FastAPI Lesson - Настройка uv"
echo "=========================================="
echo ""

# Проверка Python версии
echo "[1/5] Проверка версии Python..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

echo "Обнаружена версия Python: $PYTHON_VERSION"

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    echo "ОШИБКА: uv требует Python 3.8 или выше"
    echo "Установите Python 3.8+ и попробуйте снова"
    exit 1
fi

echo "✓ Версия Python подходит для uv"
echo ""

# Проверка установки uv
echo "[2/5] Проверка установки uv..."
if command -v uv &> /dev/null; then
    echo "✓ uv уже установлен: $(uv --version)"
else
    echo "uv не установлен. Установка..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
        export PATH="$HOME/.local/bin:$PATH"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
        export PATH="$HOME/.local/bin:$PATH"
    else
        echo "ОШИБКА: Не удалось определить ОС. Установите uv вручную:"
        echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
        exit 1
    fi
    echo "✓ uv успешно установлен"
fi
echo ""

# Создание виртуального окружения
echo "[3/5] Создание виртуального окружения..."
if [ -d ".venv" ]; then
    echo "✓ Виртуальное окружение уже существует"
else
    uv venv
    echo "✓ Виртуальное окружение создано в .venv/"
fi
echo ""

# Синхронизация зависимостей
echo "[4/5] Синхронизация зависимостей из pyproject.toml..."
uv sync
echo "✓ Зависимости установлены"
echo ""

# Проверка установки
echo "[5/5] Проверка установки..."
echo "Установленные пакеты:"
uv pip list
echo ""

# Инструкции по использованию
echo "=========================================="
echo "✓ Настройка завершена успешно!"
echo "=========================================="
echo ""
echo "Для работы с проектом выполните:"
echo ""
echo "  Активация окружения:"
echo "  source .venv/bin/activate"
echo ""
echo "  Запуск приложения:"
echo "  uv run uvicorn app.main:app --reload"
echo ""
echo "  Или после активации:"
echo "  uvicorn app.main:app --reload"
echo ""
echo "Доступные команды uv:"
echo "  uv add <пакет>           - Добавить зависимость"
echo "  uv add --dev <пакет>     - Добавить dev-зависимость"
echo "  uv sync                  - Синхронизировать зависимости"
echo "  uv run <команда>         - Запустить команду в venv"
echo "  uv pip list              - Показать установленные пакеты"
echo ""
echo "Документация доступна в README.adoc"
echo "=========================================="
