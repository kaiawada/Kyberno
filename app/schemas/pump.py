from pydantic import BaseModel, field_validator

class PumpActionSchema(BaseModel):
    action: str

    @field_validator("action")
    @classmethod
    def validate_action(cls, v: str):
        # 大文字変換し比較で、"on" でも "ON" でも受け入れ可
        upper_v = v.upper()
        if upper_v not in ["ON", "OFF"]:
            raise ValueError("Action must be 'ON' or 'OFF'")
        return upper_v