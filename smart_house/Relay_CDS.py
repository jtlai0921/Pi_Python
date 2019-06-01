from gpiozero import LightSensor
from gpiozero import LED

sensor = LightSensor(17)
relay = LED(26)
relay.on()

def light_on():
    print("It's light! :)")
    relay.on()

def light_off():
    print("It's dark! :)")
    relay.off()

while True:
    sensor.wait_for_light()
    light_on()
    sensor.wait_for_dark()
    light_off()
