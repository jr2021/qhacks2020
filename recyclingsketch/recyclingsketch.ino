#include <Stepper.h> // Include the header file

#define TOTALSTEPS 32
#define QUARTERROTATE 8


Stepper mainstepper (TOTALSTEPS, 0, 1, 2, 3);
// Stepper recyclingstepper (TOTALSTEPS, 8, 10, 9, 11);

void setup() {
  // put your setup code here, to run once:
  mainstepper.setSpeed(30);
  // recyclingstepper.setSpeed(30);
  
 //  recyclingstepper.step(512);
  mainstepper.step(512);
  delay(1500);

  mainstepper.step(-512);
 // recyclingstepper.step(-512);
}

void loop() {
  
}
