from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #Подключаем файл
    model_config = SettingsConfigDict(env_file=".env")

    # Дербаним файл на значения по названиям переменных окружения
    tmdb_api_key: str
    database_url: str

#Ругается ошибкой но на самом деле просто не понимает как работает BaseSettings
settings = Settings() # type: ignore[call-arg]
