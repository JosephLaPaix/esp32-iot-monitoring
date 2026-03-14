# 🌡️ ESP32 IoT Monitoring — Température & Humidité

Système de monitoring en temps réel avec ESP32, DHT11, MQTT, InfluxDB et Grafana.

## 🛠️ Matériel utilisé
- ESP32
- Capteur DHT11

## 🏗️ Architecture
DHT11 → ESP32 → WiFi → Mosquitto → Python → InfluxDB → Grafana

## 📦 Technologies
- Arduino IDE (programmation ESP32)
- Mosquitto (Broker MQTT)
- Python + paho-mqtt (bridge)
- InfluxDB 2.x (base de données)
- Grafana (visualisation)

## 👨‍💻 Auteur
ABANAM Essowasinam Joseph — Enseignant en Génie Électronique | Étudiant Master Big Data
```

Sauvegarde ce fichier puis envoie-le sur GitHub :
```
git add README.md
git commit -m "Ajout du README"
git push
```

---

### 🔄 Le workflow quotidien à retenir

À chaque fois que tu modifies ton code, tu fais juste ces 3 commandes :
```
git add .
git commit -m "Description de ce que tu as fait"
git push