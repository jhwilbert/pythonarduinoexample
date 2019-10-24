String str= "";

void setup() {
  Serial.begin(57600);
  pinMode(13, OUTPUT);
}

// Read the hello world string as two separate words, 
// switch on LED on pin 13 when is the world hello and switch it 
// off when is the word WORLD

void loop() {
  if (Serial.available() > 0) {
    str = Serial.readStringUntil('\n');
    Serial.println(str);
    if(str == "HELLO") {
      digitalWrite(13, HIGH);
    }
    if(str == "WORLD"){
      digitalWrite(13, LOW);
    }
    
  }
}
