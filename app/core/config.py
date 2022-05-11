import secrets
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    ALGORITHM = "HS256"
    USER_NAME = "admin"
    HASHED_PASSWORD = "$2b$12$aeT7eHQ4DssYDyRtFiXgounhOYm9GvamKJgVOo3r8FuxXNFA17INy"  # adminnimda
    DATABASE_URL: Optional[
        str
    ] = "postgres://ctfoodxx:ScEFJjefM7bodZ_s4uV_TqZ2K-1JtJg1@tai.db.elephantsql.com/ctfoodxx"

    @validator("DATABASE_URL")
    def url_adjustment(cls, DATABASE_URL):
        if "postgresql" in DATABASE_URL:
            return DATABASE_URL
        elif "postgres" in DATABASE_URL:
            return DATABASE_URL.replace("postgres", "postgresql")
        else:
            return DATABASE_URL

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:8080",
        "https://localhost:8080",
        "http://localhost",
        "https://localhost",
        "http://localhost:8081",
        "https://localhost:8081",
    ]


settings = Settings()
