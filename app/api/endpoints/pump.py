from fastapi import APIRouter, HTTPException
from app.core.config import settings
from app.schemas.pump import PumpActionSchema
import paho.mqtt.publish as publish

router = APIRouter()

@router.get("/{device_id}/{action}")
async def control_pump(device_id: str, action: str):

    try:
        validated_data = PumpActionSchema(action=action)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    topic = settings.MQTT_CMD_TOPIC_TPL.format(device_id=device_id)
    

    try:
        publish.single(
            topic,
            payload=validated_data.action,
            hostname=settings.MQTT_BROKER,
            port=settings.MQTT_PORT
        )
        return {
            "status": "Success",
            "destination": topic,
            "command": validated_data.action
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MQTT Broker connection error: {e}")