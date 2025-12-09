import functools
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_file: Path = Path(__file__).resolve().parent
    env_file: Path = app_file.joinpath(".env")

    # keyboard_main: list[list[str]] = [
    #     ["Начать смену", "Закрыть смену", "Текущая смена"],
    #     ["Начать месяц", "Завершить месяц", "Текущий месяц"],
    #     ["Графики за смену", "Графики за месяц"],
    # ]
    # keyboard_ratio: list[list[str]] = [["Ставка 5%", "Ставка 10%"]]

    TOKEN: str = "token"

    POSTGRES_HOST: str = "ludka-db"
    POSTGRES_PORT: int = 25432
    POSTGRES_USER: str = "ludka-db"
    POSTGRES_PASSWORD: str = "ludka-db"
    POSTGRES_DB: str = "ludka-db"

    RABBITMQ_HOST: str = "library-rabbitmq"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_DEFAULT_USER: str = "library-rabbitmq"
    RABBITMQ_DEFAULT_PASS: str = "library-rabbitmq"

    REDIS_HOST: str = "library-redis"
    REDIS_PORT: int = 16379
    REDIS_PASSWORD: str = "library-redis"
    REDIS_DB: int = 0

    @functools.cached_property
    def postgres_dsn(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    @functools.cached_property
    def rabbitmq_dsn(self) -> str:
        return f"amqp://{self.RABBITMQ_DEFAULT_USER}:{self.RABBITMQ_DEFAULT_PASS}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}/"

    @functools.cached_property
    def redis_dsn(self) -> str:
        return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    model_config = SettingsConfigDict(
        env_file=env_file if env_file else None,
        env_file_encoding="utf-8",
        extra="allow",
    )


@functools.lru_cache()
def settings() -> Settings:
    return Settings()
