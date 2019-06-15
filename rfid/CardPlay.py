# Appsduino RFID-RC522 接線方式 :
# RFID卡	樹莓派
# ———————————————
# IRQ	GPIO24
# RST	GPIO25
# NSS	SPICS0
# MOSI	SPIMOSI
# MISO	SPIMISO
# SCK	SPISCLK
# GND	GND
# 3.3V	3.3V
# ———————————————
# Buzeer 接線方式
# 橘線 GPIO17 (11)
# 紅線 5V
# 黑線 GND
# ———————————————

import requests
import json

firebase_url = 'https://iotfb-fc0b9.firebaseio.com/rfid'

def menu():
    print('---------------')
    print("1. 開卡")
    print("2. 讀卡")
    print("3. 消費")
    print("4. 加值")
    print("5. 離開")
    print("---------------")


def create():
    data = {'11,22,33,44,55': 0}
    result = requests.put(firebase_url + '/card.json', verify=False, data=json.dumps(data))
    print(result)

while True:
    menu()
    n = int(input('請選擇 : '))
    if(n == 1):
        print('開卡作業')
        create()
    elif (n == 2):
        print('讀卡作業')
    elif (n == 3):
        print('消費作業')
    elif (n == 4):
        print('加值作業')
    elif (n == 5):
        break

    input('按下 enter 後繼續')

