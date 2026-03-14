import json
import time
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WriteOptions
from influxdb_client.client.write_api import SYNCHRONOUS

# ─── CONFIGURATION MQTT ──────────────────────────
MQTT_BROKER  = "localhost"
MQTT_PORT    = 1883
MQTT_TOPIC   = "maison/dht11"

# ─── CONFIGURATION INFLUXDB ──────────────────────
INFLUX_URL    = "http://localhost:8086"
INFLUX_TOKEN  = "eRM2-WKl-4hbGzkvFQloUgChFgVU-zRuZm157NQviRjiF_9e461X3wfPzLObxohGcMew7kuRCnHu1Ty0YWbUfg=="       # ← On remplira ça à l'étape 6
INFLUX_ORG    = "EPL_IoT"         # ← On remplira ça à l'étape 6
INFLUX_BUCKET = "iot_data"        # ← Nom du bucket qu'on créera
# ─────────────────────────────────────────────────

# Connexion à InfluxDB
influx_client = InfluxDBClient(
    url=INFLUX_URL,
    token=INFLUX_TOKEN,
    org=INFLUX_ORG
)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connecté au broker MQTT !")
        client.subscribe(MQTT_TOPIC)
        print(f"📡 En écoute sur le topic : {MQTT_TOPIC}")
    else:
        print(f"❌ Erreur de connexion MQTT, code : {rc}")


def on_message(client, userdata, msg):
    try:
        payload     = json.loads(msg.payload.decode("utf-8"))
        temperature = payload["temperature"]
        humidite    = payload["humidite"]

        print(f"📥 Reçu → Température : {temperature}°C | Humidité : {humidite}%")

        # Ces lignes sont maintenant actives !
        point = (
            Point("dht11_mesures")
            .tag("capteur", "esp32_salon")
            .field("temperature", float(temperature))
            .field("humidite", float(humidite))
        )

        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
        print("💾 Données sauvegardées dans InfluxDB ✅")

    except Exception as e:
        print(f"❌ Erreur : {e}")


# ─── DÉMARRAGE ───────────────────────────────────
print("🚀 Démarrage du bridge MQTT → InfluxDB...")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_forever()  # Tourne en permanence