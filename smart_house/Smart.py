from gpiozero import MotionSensor, Servo, DistanceSensor, Buzzer, LED
from time import sleep
import requests
import json
import smart_house.LCD

pir = MotionSensor(18)
led = LED(20) # pir led
led2 = LED(16) # servo led
buzzer = Buzzer(21)
servo = Servo(25)
sensor = DistanceSensor(23, 24) # echo, trig
firebase_url = 'https://iotfb-fc0b9.firebaseio.com/'

smartobj = {
  "servo": "off",
  "pir": "off"
}

# init data
servo.min()
# lcd = smart_house.LCD
# lcd.lcd_init()
# lcd.lcd_string("Smart House", 0x80)
# lcd.lcd_string("Yes", 0xC0)


def warn():
    buzzer.on()
    led2.on()
    sleep(0.5)
    buzzer.off()
    led2.off()
    sleep(0.5)


def pir_on(self):
    smartobj['pir'] = 'on'
    send()
    led.on()
    buzzer.on()


def pir_off(self):
    smartobj['pir'] = 'off'
    send()
    led.off()
    buzzer.off()


def pir_service():
    pir.when_motion = pir_on
    pir.when_no_motion = pir_off


def servo_service():
    print('Distance to nearest object is', sensor.distance, 'm')
    if sensor.distance < 1.0:
        smartobj['servo'] = 'on-1'
        send()
        warn()
        smartobj['servo'] = 'on-2'
        send()
        servo.mid()
        warn()
        smartobj['servo'] = 'on-3'
        send()
        servo.max()
        warn()
        sleep(2)
        servo.min()
        smartobj['servo'] = 'off'
        send()


def send():
    msg = 'pir:%s servo:%s' % (smartobj['pir'], smartobj['servo'])
    #lcd.lcd_string(msg, 0xC0)
    result = requests.put(firebase_url + '/smart.json', verify=False, data=json.dumps(smartobj))
    print(result)


# main
while True:
    pir_service()
    servo_service()
    sleep(0.5)

