from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    project_name: str = "Synaris API"
    debug: bool = False
    database_url: AnyUrl
    auth_secret: str
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440
    cookie_name: str = "synaris_session_token"
    cookie_domain: str | None = None
    app_url: str = "http://localhost:3000"
    oauth_redirect_uri: str | None = None

    openrouter_api_key: str | None = None
    openrouter_model: str = "gpt-4o-mini"
    groq_api_key: str | None = None
    groq_model: str = "groq-1.5-mini"
    gemini_api_key: str | None = None
    gemini_model: str = "gemini-1.5-mini"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
