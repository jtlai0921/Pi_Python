from gpiozero import LightSensor
from time import sleep

sensor = LightSensor(17)

while True:
    print(sensor.value)
    sleep(1)


