from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
   
    PROJECT_NAME: str
    LOCATION: str
    MQTT_BROKER: str
    MQTT_PORT: int


    @property
    def MQTT_CMD_TOPIC_TPL(self) -> str:
        
        return f"{self.PROJECT_NAME}/{self.LOCATION}/{{device_id}}/cmd"

    @property
    def MQTT_STATUS_TOPIC_TPL(self) -> str:
        return f"{self.PROJECT_NAME}/{self.LOCATION}/{{device_id}}/status"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()