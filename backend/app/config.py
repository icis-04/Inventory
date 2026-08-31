import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./parts_ledger.db")
    PHOTO_DIR: str = os.getenv("PHOTO_DIR", "./photo_storage")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

settings = Settings()

os.makedirs(settings.PHOTO_DIR, exist_ok=True)
