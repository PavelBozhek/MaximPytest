from pydantic.v1 import BaseSettings


class Configuration(BaseSettings):
    service_url: str

    class Config:
        env_file = ".env"