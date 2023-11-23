import os
from dotenv import dotenv_values

env_file = dotenv_values(".env")

class Config:
    DEBUG = env_file.get("DEBUG") or os.getenv("DEBUG", True)
    LOG_LEVEL = env_file.get("LOG_LEVEL")
    LOG_FILE = env_file.get("LOG_FILE")

config = Config()
