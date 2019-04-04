#include <ArduinoJson.h>
#include <OneWire.h> 
#include <DallasTemperature.h>
#define ONE_WIRE_BUS 2 
OneWire oneWire(ONE_WIRE_BUS); 
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(115200);
   sensors.begin(); 
}

void loop() {
  sensors.requestTemperatures();
  
  DynamicJsonDocument doc(1024);
  
  doc["sensor"] = sensors.getTempCByIndex(0);
  doc["time"] = millis();
  serializeJson(doc, Serial);
  Serial.println();
  delay(100);
}
