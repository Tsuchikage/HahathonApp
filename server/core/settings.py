import os
from pydantic import model_validator
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    APP_TITLE: str = "FastAPI JWT Auth API"
    VERSION: str = "1.0.0"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    # REFRESH_TOKEN_EXPIRE_DAYS: int = 30
    JWT_SECRET: str = "d1fe428d-1b8b-47a2-bef1-660329781d5074457a17-8cc8-451b-aff5-06bf6cb4aee4"
    JWT_ALGORITHM: str = "HS256"

    POSTGRES_USER: str = "user"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "database"
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str = "postgresql://user:password@postgres:5432/database"

    # "postgresql://user:password@localhost:5432/database"
    @model_validator(mode="after")
    def validator(cls, values: "Settings") -> "Settings":
        values.DATABASE_URL = (
            f"{values.POSTGRES_USER}:{values.POSTGRES_PASSWORD}@"
            f"{values.POSTGRES_HOST}:{values.POSTGRES_PORT}/{values.POSTGRES_DB}"
        )
        return values


def get_settings():
    return Settings()


settings = get_settings()
