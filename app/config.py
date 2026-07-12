from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FinOps AI Platform"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"


settings = Settings()