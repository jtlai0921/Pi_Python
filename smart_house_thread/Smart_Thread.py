from gpiozero import MotionSensor, Servo, DistanceSensor, Buzzer, LED, LightSensor, MCP3008
from RPLCD.i2c import CharLCD
import _thread
import time
import requests
import json

# 感測器
pir       = MotionSensor(18)
pir_led   = LED(20) # pir led
servo = Servo(25)
sensor = DistanceSensor(23, 24) # echo, trig
buzzer = Buzzer(21)
servo_led = LED(16)
cds_sensor = LightSensor(17)
relay = LED(26)
lm35 = MCP3008(channel=1)
lcd = CharLCD('PCF8574', address=0x3f, port=1, backlight_enabled=True)
pot = MCP3008(0)

# 感測器初始狀態
servo.min()
relay.on()
lcd.clear()

# 變數定義
firebase_url = 'https://iotfb-fc0b9.firebaseio.com/'
smartcontrolobj = {
    "cds_relay": "on",
    "relay": "off"
}
smartobj = {
    "pir": "off",
    "servo": "off",
    "distance": "0",
    "cds":"off",
    "lm35": 0.0,
    "pot": 0.0,
}

# 1.PIR ------------------------------------------------------
def pir_on(self):
    smartobj['pir'] = 'on'
    pir_led.on()

def pir_off(self):
    smartobj['pir'] = 'off'
    pir_led.off()

def run_pir( threadName, delay):
   while True:
      time.sleep(delay)
      pir.when_motion = pir_on
      pir.when_no_motion = pir_off
      send()
      print ("%s: %s %s" % ( threadName, time.ctime(time.time()), smartobj ))

# 2.DistanceSensor + Buzeer + Servo -----------------------------------------------
def warn():
    buzzer.on()
    servo_led.on()
    time.sleep(0.5)
    buzzer.off()
    servo_led.off()
    time.sleep(0.5)

def run_distance( threadName, delay):
   time.sleep(delay)
   while True:
       print('Distance to nearest object is', sensor.distance, 'm')
       if sensor.distance < 1.0:
           smartobj['distance'] = sensor.distance
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
           time.sleep(2)
           servo.min()
           smartobj['servo'] = 'off'
           send()
       time.sleep(1)


# 3.CDS + Relay -----------------------------------------------
def cds_on():
    print("It's light! :)")
    smartobj['cds'] = 'on'
    send()
    if (json.loads(getControlJson())['cds_relay'] == 'on'):
        relay.on()

def cds_off():
    print("It's dark! :)")
    smartobj['cds'] = 'off'
    send()
    if (json.loads(getControlJson())['cds_relay'] == 'on'):
        relay.off()

def run_cds(threadName, delay):
    time.sleep(delay)
    while True:
        cds_sensor.wait_for_light()
        cds_on()
        cds_sensor.wait_for_dark()
        cds_off()


# 4.LM35 + LCD -----------------------------------------------
def convert_temp(gen):
    for value in gen:
        print('value=', value)
        yield value * 3.3 * 100


def run_lm35(threadName, delay):
    time.sleep(delay)
    for temp in convert_temp(lm35.values):
        print('The temp is ', temp, ' C')
        lcd.cursor_pos = (0, 0)
        lcd.write_string('Temp %.2f C' % temp)
        smartobj['lm35'] = temp
        send()
        time.sleep(1)


# 5.Pot + LED -----------------------------------------------
def run_pot(threadName, delay):
    time.sleep(delay)
    while True:
        print(pot.value)
        smartobj['pot'] = pot.value
        time.sleep(0.5)


# 5.Listener control -----------------------------------------------
def run_listener_control(threadName, delay):
    time.sleep(delay)
    while True:
        if (json.loads(getControlJson())['cds_relay'] == 'off'):
            if (json.loads(getControlJson())['relay'] == 'off'):
                relay.on()
            else:
                relay.off()
        time.sleep(0.5)


# 7.1 Send to firebase -----------------------------------------------
def send():
    result = requests.put(firebase_url + '/smart_thread.json', verify=False, data=json.dumps(smartobj))
    print(result)
    pass

# 7.2 Send to firebase init smart_thread_control ----------------------
def send_init_smartcontrolobj():
    result = requests.put(firebase_url + '/smart_thread_control.json', verify=False, data=json.dumps(smartcontrolobj))
    print(result)
    pass

# 8.Get from firebase -----------------------------------------------
def getControlJson():
    result = requests.get(firebase_url + '/smart_thread_control.json')
    return result.text

# 主程式 -------------------------------------------------------------
# 初始 smart_thread_control
send_init_smartcontrolobj()
time.sleep(3)
try:
    _thread.start_new_thread(run_pir, ("PIR", 1,))
    _thread.start_new_thread(run_cds, ("CDS", 1,))
    _thread.start_new_thread(run_lm35, ("LM35", 1,))
    _thread.start_new_thread(run_pot, ("POT", 1,))
    _thread.start_new_thread(run_listener_control, ("Control", 1,))

except:
   print ("Error: ")

while True:
    run_distance("Distance", 1)
    pass

