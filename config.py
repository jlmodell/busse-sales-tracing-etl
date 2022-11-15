from decouple import config
from pydantic import BaseModel


class Settings(BaseModel):
    mongodb_uri: str = config("MONGODB_URI")

    mail_server: str = config("MAIL_SERVER")
    mail_username: str = config("MAIL_USERNAME")
    mail_password: str = config("MAIL_PASSWORD")
    mail_port: int = config("MAIL_PORT")
    mail_sender: str = config("MAIL_SENDER")


CONFIG = Settings()
