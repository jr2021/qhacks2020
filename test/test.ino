#include <Stepper.h>
int t =0;
const int stepsPerRevolution = 2038;  // change this to fit the number of steps per revolution 
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);
Stepper myStepperRecycling(stepsPerRevolution, 3, 4, 5, 6);


int stepCount = 0;  // number of steps the motor has taken

void setup() {
  myStepper.setSpeed(6);
  myStepperRecycling.setSpeed(6);
}

void loop() {
  // read the sensor value:
  // step 1/100 of a revolution:
    myStepper.step(510);
    myStepperRecycling.step(510);
    delay(1000);
}
