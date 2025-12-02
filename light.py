import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

resistorPin = 7

while True:
    GPIO.setup(resistorPin, GPIO.OUT)
    GPIO.output(resistorPin, GPIO.LOW)
    time.sleep(0.1)
    
print("hi")