import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_URL: str = str(os.getenv("API_URL", "http://localhost:8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    API_KEY_HEADER: str = os.getenv("API_KEY_HEADER", "X-Api-Key")
    API_KEY: str = os.getenv("API_KEY", "test")
    API_UPLOAD_PATH: str = os.getenv("API_UPLOAD_PATH", "/images/upload")
    API_PREDICT_PATH: str = os.getenv("API_PREDICT_PATH", "/images/predict")

    class Config:
        if os.path.exists("../.env"):
            env_file = "../.env"
            env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()
