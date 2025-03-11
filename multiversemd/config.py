from pydantic import BaseSettings

class Settings(BaseSettings):
    default_model: str = "gpt-3.5-turbo"

