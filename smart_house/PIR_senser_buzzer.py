from gpiozero import MotionSensor, Buzzer, LED
from signal import pause

pir = MotionSensor(18)
led = LED(16)
buzzer = Buzzer(21)

def on(self):
    led.on()
    buzzer.on()

def off(self):
    led.off()
    buzzer.off()

pir.when_motion = on
pir.when_no_motion = off

pause()