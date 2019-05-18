from gpiozero import PWMLED
from time import sleep

pwmled = PWMLED(24)
pwmled.blink(1, 1, 0, 0, 3, False)
sleep(3)
pwmled.pulse(3, 3, 3, False)
