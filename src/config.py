import os
from pathlib import Path
from pydantic import Field
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # model_config = SettingsConfigDict(env_file=Path(os.path.dirname(os.path.realpath(__file__))) / '.env',
    #                                   env_file_encoding='utf-8')

    MS_HOST: str = Field("0.0.0.0", validation_alias="MS_HOST", env="MS_HOST")
    MS_PORT: int = Field(8080, validation_alias="MS_PORT", env="MS_PORT")

    MS_LOG_LEVEL: str = Field("INFO", validation_alias="MS_LOG_LEVEL", env="MS_LOG_LEVEL")
    MS_LOG_FILE: Optional[str] = Field(None, validation_alias="MS_LOG_FILE", env="MS_LOG_FILE")

    MAIL_SERVER: str = Field("smtp.gmail.com", validation_alias="MAIL_SERVER", env="MAIL_SERVER")
    MAIL_PORT: int = Field(465, validation_alias="MAIL_PORT", env="MAIL_PORT")

    MAIL_USER: str = Field("user@mail.ru", validation_alias="MAIL_USER", env="MAIL_USER")
    MAIL_PASSWORD: str = Field("password", validation_alias="MAIL_PASSWORD", env="MAIL_PASSWORD")


config = Config()
