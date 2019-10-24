int sensorValue1= 0;
int sensorValue2= 0;


void setup() {
  
  Serial.begin(57600);
 
}

void loop() {

    // Sending Integer to Python
    sensorValue1 += 1;
    Serial.write(sensorValue1 / 256);
    Serial.write(sensorValue1 % 256);

    sensorValue2 += 10;
    Serial.write(sensorValue2 / 256);
    Serial.write(sensorValue2 % 256);

}
