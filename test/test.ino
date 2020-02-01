#include <Stepper.h>
int t =0;
const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor


// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

int stepCount = 0;  // number of steps the motor has taken

void setup() {
  Serial.begin(9600);
}

void loop() {
  // read the sensor value:
  //int sensorReading = analogRead(A0);
  // map it to a range from 0 to 25:
  //int motorSpeed = map(sensorReading, 0, 1023, 0, 25);
  // set the motor speed:
  int motorSpeed = 15;
  if (motorSpeed > 0) {
    myStepper.setSpeed(motorSpeed);
    // step 1/100 of a revolution:
    myStepper.step(100);
  Serial.println(motorSpeed);//print how fast the motor is going in the serial monitor
  }
}
