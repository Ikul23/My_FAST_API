import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(file).parent.parent
ATTACHMENT_DIR = os.path.join(BASE_DIR, "src", "attachment", "storage")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, "./.env"))

    POSTGRES_DB_USER_TEST: str
    POSTGRES_DB_PASSWORD_TEST: int
    POSTGRES_DB_HOST_PORT_TEST: str
    POSTGRES_DB_HOST_TEST: str
    POSTGRES_DB_NAME_TEST: str

    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}"
