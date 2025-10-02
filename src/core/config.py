from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    """Loads the dotenv file. Including this is necessary to get
    pydantic to load a .env file."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Config(BaseConfig):
    APP_NAME: str = "App Name"
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    DB_URL: str
    # DB_FORCE_ROLL_BACK: bool = False


def get_config(env_state):
    """Instantiate config based on the environment."""
    return Config()


config = get_config(BaseConfig())
