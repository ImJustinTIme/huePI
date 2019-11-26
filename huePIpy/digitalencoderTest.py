from RPi import GPIO
from time import sleep
from KY040 import KY040
import requests
import phue 

clk1 = 18
dt1 = 15
switch1 = 14
led = 22
URL = "http://192.168.1.78/api/8ei4C7jnWgPbD9JpcqQb5dmGAZPdZblNOgtZQX4b/"



def rotaryChanged(dir):
        if dir == 0:
                if g1.brightness-20 <= 1:
                        g1.brightness = 1
                        print("already at lowest")
                else:
                        g1.brightness = g1.brightness - 20

        else:
                
                if g1.brightness+20 >= 254:
                        g1.brightness = 254
                        print("already at highest")
                else:
                        g1.brightness = g1.brightness + 20
        
        print("turned brightness to: "+ str(g1.brightness))

def switchPressed():
        
        g1.on = not g1.on
        #GPIO.output(led , not GPIO.input(led))
        
        print("Lights on: "+str(g1.on))
        

    


ky040 = KY040(clk1, dt1, switch1, rotaryChanged, switchPressed)
ky040.start();
GPIO.setmode(GPIO.BCM)


b = phue.Bridge(ip='192.168.1.78',username='8ei4C7jnWgPbD9JpcqQb5dmGAZPdZblNOgtZQX4b')
#b.connect()
g1 = phue.Group(b,1)




try:
        while True:
                sleep(.01)
          

finally:
        ky040.stop()
        GPIO.cleanup()