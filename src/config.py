import os
from dotenv import dotenv_values
from common.utils import str_to_bool

env_file = dotenv_values(".env")

class Config:
    DEBUG = str_to_bool(env_file.get("APP_DEBUG"), True)
    LOG_LEVEL = env_file.get("LOG_LEVEL") or "INFO"
    LOG_FILE = env_file.get("LOG_FILE") or './logs/app.log'

config = Config()

__all__ = [config]
