int brightness = 0;
const int pin = 13;

void setup() {
  pinMode(pin, OUTPUT);
  Serial.begin(57200);  
}

void loop() {
  if (Serial.available() > 0) {
    brightness = Serial.read();
    analogWrite(pin, brightness);
  }
}
