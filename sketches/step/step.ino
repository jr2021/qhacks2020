#include <Stepper.h>
const int stepsPerRevolution = 2038;  // change this to fit the number of steps per revolution

int stepCount = 0;  // number of steps the motor has taken

void setup() {
  // initialize the stepper library on pins 8 through 11:
  iteratefirst(10, 13);
  iteratesecond(3,4);
  delay(2000);
  //
  iteratefirst(13, 10);
  iteratesecond(4,3);
}

void iteratefirst(int Aplus, int Aminus) {
  Stepper myStepper(stepsPerRevolution, Aplus, 11, 12, Aminus);
  myStepper.setSpeed(6);
  // read the sensor value:
  myStepper.step(510);
}

void iteratesecond(int Aplus, int Aminus) {
  Stepper myStepper(stepsPerRevolution, Aplus, Aminus, 5, 6);
  myStepper.setSpeed(6);
  // read the sensor value:
  myStepper.step(510);
}

void loop() {
  
}
