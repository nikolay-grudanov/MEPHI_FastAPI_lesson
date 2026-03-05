"""Конфигурация FastAPI приложения."""

from fastapi import FastAPI

from .handlers import router


def get_application() -> FastAPI:
    """Создаёт и возвращает экземпляр FastAPI приложения.

    Returns:
        FastAPI: Экземпляр приложения с подключённым маршрутизатором
    """
    application = FastAPI()
    application.include_router(router)
    return application


app = get_application()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
