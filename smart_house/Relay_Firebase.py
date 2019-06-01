from gpiozero import LED
from time import sleep
import requests
import json

relay = LED(26)
relay.on()

while True:
    result = requests.get('https://iotfb-fc0b9.firebaseio.com/control.json')
    if (json.loads(result.text)['light'] == 1):
        print('開燈')
        relay.off()
    else:
        print('關燈')
        relay.on()
    sleep(1)

