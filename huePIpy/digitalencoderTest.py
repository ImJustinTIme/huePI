from RPi import GPIO
from time import sleep
from KY040 import KY040



clk1 = 18
dt1 = 15
switch1 = 14
led = 22




def rotaryChanged(dir):
        print("turned - " + str(dir))

def switchPressed():
        GPIO.output(led , not GPIO.input(led))
        
        print("button pressed " + str(GPIO.input(led)))
        

    


ky040 = KY040(clk1, dt1, switch1, rotaryChanged, switchPressed)
ky040.start();
GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)

try:
        while True:
                sleep(.01)
          

finally:
        ky040.stop()
        GPIO.cleanup()