from gpiozero import RGBLED
from time import sleep
from random import randint

led = RGBLED(red=17, green=27, blue=22)
for n in range(10):
    r = randint(1, 100) / 100
    g = randint(1, 100) / 100
    b = randint(1, 100) / 100
    led.color = (r, g, b)
    sleep(1)
