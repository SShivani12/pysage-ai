import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "PySage AI"
    APP_VERSION = "0.1.0"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


settings = Settings()