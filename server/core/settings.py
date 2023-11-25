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

    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')
    # REFRESH_TOKEN_EXPIRE_DAYS: int = os.getenv('REFRESH_TOKEN_EXPIRE_DAYS')
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM')

    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_NAME: str = os.getenv('POSTGRES_NAME')
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT: int = os.getenv('POSTGRES_PORT')
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"

    @model_validator(mode="after")
    def validator(cls, values: "Settings") -> "Settings":
        values.DATABASE_URL = (
            f"{values.POSTGRES_USER}:{values.POSTGRES_PASSWORD}@"
            f"{values.POSTGRES_HOST}:{values.POSTGRES_PORT}/{values.POSTGRES_NAME}"
        )
        return values


def get_settings():
    return Settings()


settings = get_settings()
