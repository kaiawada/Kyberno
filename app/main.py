from fastapi import FastAPI
import paho.mqtt.client as mqtt

app = FastAPI()

MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_TOPIC = "kyberno/grc/pump001"

client = mqtt.Client()

# 起動時に一度だけMQTTブローカーに接続する
try:
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()  # 通信を裏で開始
    print("MQTT Broker Connected!")
except Exception as e:
    print(f"MQTT Connection Failed: {e}")

    # --- API設定 ---

@app.get("/")
def read_root():
    return {"System": "Kyberno", "Status": "Online", "Location": "Greece"}

@app.get("/pump/{action}")
def control_pump(action: str):

    if action not in ["ON", "OFF"]:
        return {"error": "Invalid action. Use ON or OFF"}
    

    client.publish(MQTT_TOPIC, action)
    
    return {
        "device": "pump_main",
        "action": action,
        "mqtt_topic": MQTT_TOPIC,
        "status": "Message Sent"
    }
