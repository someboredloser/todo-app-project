from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    env: str = "dev"
    debug: bool = False

    database_url: str
    secret_key: str

    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7

    cors_origins: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )

    @property
    def cors_origins_list(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]


settings = Settings()