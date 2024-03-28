# IoT-assignment

This Python script facilitates the simulation of sensor data transmission to the ThingSpeak platform via the MQTT protocol. The following steps outline how to configure and utilize this script effectively:

### Configuration Steps:

1. **Create ThingSpeak Account:**
   If you do not have an existing ThingSpeak account, visit [ThingSpeak website](https://thingspeak.com/login?skipSSOCheck=true) to create one.

2. **Create ThingSpeak Channel:**
   Navigate to the "Channels" section on ThingSpeak and click on “New Channel” to create a Channel.

3. **Add MQTT Device:**
   Access the devices menu, select MQTT, and then "Add a New Device." Connect the channel created earlier to the device to complete the setup.

4. **Update Script Variables:**
   Modify the script variables `MQTT_CLIENT_ID_CUSTOM`, `MQTT_USER_CUSTOM`, `MQTT_PASSWORD_CUSTOM`, `MQTT_SERVER_CUSTOM`, `MQTT_PORT_CUSTOM`, `MQTT_TOPIC_TEMPERATURE_CUSTOM`, `MQTT_TOPIC_HUMIDITY_CUSTOM`, `MQTT_TOPIC_CO2_CUSTOM`, `WIFI_SSID_CUSTOM`, and `WIFI_PASSWORD_CUSTOM` with appropriate values according to your ThingSpeak account and Wi-Fi network credentials.

### Running the Script:

1. **Run the Script:**
   Execute the Python script on your device.

2. **Wi-Fi Connection:**
   The script will attempt to connect to the specified Wi-Fi network using the provided credentials.

3. **Sensor Data Publishing:**
   Once connected to Wi-Fi, the script enters a loop to continuously generate sensor data (temperature, humidity, and CO2), establish a connection with the MQTT broker, and publish this data to the relevant ThingSpeak channel fields.

### Notes:

- Ensure that the specified Wi-Fi network is available and accessible by the device running the script.
- Verify that the MQTT broker details and ThingSpeak channel configurations are accurately reflected in the script variables.
- Adjust the frequency of data publishing (currently set to every 5 seconds) as needed.

By following these steps, you can effectively simulate sensor data transmission to ThingSpeak and monitor sensor readings in real-time.
