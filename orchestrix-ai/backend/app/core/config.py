from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Orchestrix AI API"
    environment: str = "development"
    debug: bool = True

    api_prefix: str = "/api"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24

    postgres_url: str = "postgresql://postgres:postgres@localhost:5432/orchestrix"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "gemma3"
    chroma_host: str = "localhost"
    chroma_port: int = 8001
    chroma_collection: str = "orchestrix_memory"

    tts_engine: str = "pyttsx3"
    whisper_model: str = "base"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
