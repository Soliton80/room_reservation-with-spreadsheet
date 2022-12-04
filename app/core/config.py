from pydantic import BaseSettings, EmailStr
from typing import Optional



class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    app_description: str = 'приложение предоставит возможность бронировать помещения на определённый период времени'
    database_url: str
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    
    class Config:
        env_file = '.env'


settings = Settings()