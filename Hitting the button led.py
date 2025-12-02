import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.IN)

GPIO.setup(4,GPIO.OUT)

print('started')

while True:
    input=GPIO.input(17)
    if (GPIO.input(17)==True):
        GPIO.output(4,True)
        time.sleep(2)
        print ('Button Hit')
    else:
        GPIO.output (4,False)
    time.sleep(0.1) 
    
print('end')