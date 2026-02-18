from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "DevMetrics API"
    environment: str = "dev"

settings = Settings()
