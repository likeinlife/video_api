from functools import partial

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

_model_config = partial(SettingsConfigDict, env_file=".env", extra="ignore")


class DBSettings(BaseSettings):
    model_config = _model_config(env_prefix="DB_")

    password: SecretStr = Field(init=False)
    user: SecretStr = Field(init=False)
    host: str = Field(init=False)
    port: int = Field(default=5432, init=False)
    db_name: str = Field(default="video", init=False)

    def get_url(self, async_: bool = True) -> str:
        driver = "asyncpg" if async_ else "psycopg2"
        return (
            f"postgresql+{driver}://{self.user.get_secret_value()}:"
            f"{self.password.get_secret_value()}@{self.host}:{self.port}/{self.db_name}"
        )


class LoggingSettings(BaseSettings):
    model_config = _model_config(env_prefix="LOGGING_")

    level: str = Field(default="INFO", init=False)
    json_format: bool = Field(default=False, init=False)


class SessionSettings(BaseSettings):
    model_config = _model_config(env_prefix="FARPOST_")

    ttl: int = Field(default=60 * 60, init=False)


class AppSettings(BaseSettings):
    model_config = _model_config(env_prefix="APP_")

    name: str = Field(init=False)
    version: str = Field(init=False)
    debug: bool = Field(default=False, init=False)


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DBSettings = DBSettings()
    log: LoggingSettings = LoggingSettings()
    session: SessionSettings = SessionSettings()


settings = Settings()
