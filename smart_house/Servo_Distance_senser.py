from gpiozero import Servo, DistanceSensor, Buzzer, LED
from time import sleep

servo = Servo(25)
sensor = DistanceSensor(23, 24) # echo, trig
buzzer = Buzzer(21)
led = LED(16)

servo.min()

def warn():
    buzzer.on()
    led.on()
    sleep(0.5)
    buzzer.off()
    led.off()
    sleep(0.5)

while True:
    print('Distance to nearest object is', sensor.distance, 'm')
    if sensor.distance < 1.0 :
        warn()
        servo.mid()
        warn()
        servo.max()
        warn()
        sleep(2)
        servo.min()
    sleep(0.5)
