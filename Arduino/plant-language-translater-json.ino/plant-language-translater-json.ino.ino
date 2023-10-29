#include "dht.h"
#include <ArduinoJson.h>

#define dht_apin A1 // Analog Pin sensor is connected to
#define sensor_pin A0

dht DHT;

void setup() {
  Serial.begin(9600);
  pinMode(sensor_pin, INPUT);
  delay(500); // Delay to let the system boot
  Serial.println("Plant Sensor\n");
  delay(1000); // Wait before accessing the sensors
}

int mapSoilMoisture(int sensorValue) {
  // Map the sensor value from the 0-1023 range to the 0-100 range
  int percentage = map(sensorValue, 1023, 340, 0, 100);

  percentage = constrain(percentage, 0, 100);

  return percentage;
}

void loop() {
  // Read soil moisture
  int sensorValue = analogRead(sensor_pin);
  int moisturePercentage = mapSoilMoisture(sensorValue);

  // Read temperature and humidity
  DHT.read11(dht_apin);

  // Create a JSON object to store the data
  DynamicJsonDocument jsonDoc(200); // Adjust the buffer size as needed

  // Store temperature data in JSON
  JsonObject tempData = jsonDoc.createNestedObject("temp");
  tempData["value"] = DHT.temperature;
  if (DHT.temperature >= 30) {
    tempData["msg"] = "It's getting hot in here! Please provide some shade.";
  } else if (DHT.temperature >= 20) {
    tempData["msg"] = "Ah, the temperature is just right. Thanks for keeping me comfortable!";
  }

  // Store humidity data in JSON
  JsonObject humidityData = jsonDoc.createNestedObject("humidity");
  humidityData["value"] = DHT.humidity;
  if (DHT.humidity >= 70) {
    humidityData["msg"] = "It's so humid! Please, a bit less moisture in the air.";
  } else if (DHT.humidity >= 40) {
    humidityData["msg"] = "Perfect humidity level. Thanks for keeping me cozy!";
  } else {
    humidityData["msg"] = "It's too dry! Can you please humidify the air a bit?";
  }

  // Store moisture data in JSON
  JsonObject moistureData = jsonDoc.createNestedObject("moisture");
  moistureData["value"] = moisturePercentage;
  if (moisturePercentage >= 80) {
    moistureData["msg"] = "It's so wet! No more water, please!";
  } else if (moisturePercentage >= 60) {
    moistureData["msg"] = "Ah, perfect moisture levels. Thanks for taking care of me!";
  } else {
    moistureData["msg"] = "I'm starting to feel a bit thirsty. A little drink would be nice.";
  }

  // Serialize the JSON to a string
  String jsonString;
  serializeJson(jsonDoc, jsonString);

  // Print the JSON to the Serial port
  Serial.println(jsonString);

  delay(1000); // Wait 5 seconds before the next reading
}
