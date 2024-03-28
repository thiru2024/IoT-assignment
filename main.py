"""
MicroPython IoT Weather Station Example for Wokwi.com

To view the data:

1. Go to http://www.hivemq.com/demos/websocket-client/
2. Click "Connect"
3. Under Subscriptions, click "Add New Topic Subscription"
4. In the Topic field, type "wokwi-weather" then click "Subscribe"

Now click on the DHT22 sensor in the simulation,
change the temperature/humidity, and you should see
the message appear on the MQTT Broker, in the "Messages" pane.

Copyright (C) 2022, Uri Shaked

https://wokwi.com/arduino/projects/322577683855704658
"""

import network
import time
import urandom
from umqtt.simple import MQTTClient

# MQTT broker details of Thingspeak
MQTT_CLIENT_ID_CUSTOM = "GSMxLTETMgERDAkvMSIPNBo"
MQTT_USER_CUSTOM = "GSMxLTETMgERDAkvMSIPNBo"
MQTT_PASSWORD_CUSTOM = "YApAQpdNiPM2DEQcMG0hAuLv"
MQTT_SERVER_CUSTOM = "mqtt3.thingspeak.com"
MQTT_PORT_CUSTOM = 1883
MQTT_TOPIC_TEMPERATURE_CUSTOM = "channels/2488587/publish/fields/field1"
MQTT_TOPIC_HUMIDITY_CUSTOM = "channels/2488587/publish/fields/field2"
MQTT_TOPIC_CO2_CUSTOM = "channels/2488587/publish/fields/field3"

WIFI_SSID_CUSTOM = "Wokwi-GUEST"
WIFI_PASSWORD_CUSTOM = ""

def sensordata():
    temperature = urandom.uniform(-50, 50)
    humidity = urandom.uniform(0, 100)
    co2 = urandom.uniform(300, 2000)
    return temperature, humidity, co2

# Publish data
def publish(temperature, humidity, co2):
    client = MQTTClient(MQTT_CLIENT_ID_CUSTOM, MQTT_SERVER_CUSTOM, user=MQTT_USER_CUSTOM, password=MQTT_PASSWORD_CUSTOM)
    client.connect()
    client.publish(MQTT_TOPIC_CO2_CUSTOM, str(co2))
    client.publish(MQTT_TOPIC_HUMIDITY_CUSTOM, str(humidity))
    client.publish(MQTT_TOPIC_TEMPERATURE_CUSTOM, str(temperature))
    client.disconnect()

# Wi-Fi
WIFI_INTERFACE_CUSTOM = network.WLAN(network.STA_IF)
WIFI_INTERFACE_CUSTOM.active(True)
WIFI_INTERFACE_CUSTOM.connect(WIFI_SSID_CUSTOM, WIFI_PASSWORD_CUSTOM)

while not WIFI_INTERFACE_CUSTOM.isconnected():
    pass

print("Wi-Fi connection established")

# Publishing sensor data
while True:
    temperature, humidity, co2 = sensordata()
    publish(temperature, humidity, co2)
    print("Published: Temperature={:.2f}C, Humidity={:.2f}%, CO2={:.2f}ppm".format(temperature, humidity, co2))
    time.sleep(5)
