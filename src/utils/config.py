"""
Application configuration.

Loads environment variables from .env and exposes them
through a single configuration object.

Author: Simba Munatsi
Project: PayFlow Intelligence Platform
"""

from dataclasses import dataclass
import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()


@dataclass(frozen=True)
class Config:
    """
    Central application configuration.
    """

    # Application
    APP_NAME: str = os.getenv("APP_NAME", "PayFlow Intelligence Platform")
    APP_ENV: str = os.getenv("APP_ENV", "development")

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Database
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME", "payflow")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")

    # AI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    # Pipeline
    PIPELINE_BATCH_SIZE: int = int(
        os.getenv("PIPELINE_BATCH_SIZE", 10000)
    )


config = Config()