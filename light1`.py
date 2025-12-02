import time
import RPi.GPIO as GPIO

  analogValue = analogRead(A0);

  print("Analog reading = "+ analogValue);
  print(analogValue);   

  if (analogValue < 100) {
    print(" - Very bright");
  } else if (analogValue < 200) {
    print(" - Bright");
  } else if (analogValue < 500) {
    print(" - Light");
  } else if (analogValue < 800) {
    print(" - Dim");
  } else {
    print(" - Dark");
  }
  delay(1);
