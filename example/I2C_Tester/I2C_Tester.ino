
#include <Wire.h>

void setup() {
  Wire.begin(8);
  Wire.onReceive(receiveEvent);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  delay(100);
}

void receiveEvent(int howMany) {
  while (Wire.available()) {
    char c = Wire.read();
    digitalWrite(LED_BUILTIN, c);
  }
}
