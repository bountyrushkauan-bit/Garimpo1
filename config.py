import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "Garimpeiro PCW")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./garimpeiro.db")
    scrape_enabled: bool = os.getenv("SCRAPE_ENABLED", "false").lower() == "true"

settings = Settings()
