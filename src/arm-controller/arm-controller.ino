// For Arduino Uno
// Provide 6 registers to be controlled by the Raspberry
// Pi via I2C for controlling the arm servos.
// Servo signal pins:
// JO: pin 3
// J1: pin 5
// J2: pin 6
// J3: pin 9
// J4: pin 10
// J5: pin 11
// See Arduino Uno pinout diagram for SDA and SCL (I2C) pins.

#include <Wire.h>
#include <Servo.h>

// Index corresponds to joint label number.
Servo servos[6];
int servoHomeAngles[] = {90, 150, 20, 0, 0, 0};
int servoHomeAnglesSize = sizeof(servoHomeAngles)/sizeof(int);
 
void setup() {
  // I2C setup
  Wire.begin(8);
  Wire.onReceive(receiveEvent);

  // Servo setup
  servos[0].attach(3);
  servos[1].attach(5);
  servos[2].attach(6);
  servos[3].attach(9);
  servos[4].attach(10);
  servos[5].attach(11);

  // Set servos to home angles
  for (int i = 0; i < servoHomeAnglesSize; i++) {
    writeServo(i, servoHomeAngles[i]);
  }
}

void loop() {
  delay(100);
}

// Protocol: first byte sent is which servo to set.
// Second byte is the new angle value.
void receiveEvent(int numBytes) {
  while (Wire.available() > 0){
    servo = Wire.read();
    angle = Wire.read();
    writeServo(servo, angle);
  }
}

void writeServo(int servo, int newAngle) {
  servos[servo].write(newAngle);
}
