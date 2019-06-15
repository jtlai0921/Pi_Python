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
import signal
import time
import sys
import RPi.GPIO as GPIO
from pirc522 import RFID
import urllib3

urllib3.disable_warnings() # 移除 SSL 警告
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
buzeer = GPIO.PWM(32, 50) # GPIO.PWM(channel, frequency)
firebase_url = 'https://iotfb-fc0b9.firebaseio.com/rfid'

fee = 30

def menu():
    print('---------------')
    print("1. 開卡")
    print("2. 讀卡")
    print("3. 消費")
    print("4. 加值")
    print("5. 離開")
    print("---------------")

def getCardId():
    print('請感應卡片')
    rdr.wait_for_tag()
    (error, data) = rdr.request()
    # if error:
    #     print("Read Error")

    (error, uid) = rdr.anticoll()
    if not error:
        cardId = str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3])
        print("Card read UID: " + cardId)
        buzeer.ChangeFrequency(1)  # set frequency
        buzeer.start(10)  # 占空比 (0.0 <= dc <= 100.0)
        time.sleep(0.1)  # for buzeer
        buzeer.stop()
        return cardId

def create():
    cardId = getCardId()
    result = requests.get(firebase_url + '/' + cardId + '.json')
    if json.loads(result.text) == None:
        data = {'cash': 0}
        result = requests.put(firebase_url + '/' + cardId + '.json', verify=False, data=json.dumps(data))
        print('卡片 ' + cardId + ' 開卡成功')
    else:
        print('卡片 ' + cardId + ' 已開過卡')


def read():
    cardId = getCardId()
    result = requests.get(firebase_url + '/' + cardId + '.json')
    try:
        cash = json.loads(result.text)['cash']
        print(cardId, cash)
    except:
        print('找無此卡, 請先進入開卡作業')


def consumer():
    cardId = getCardId()
    result = requests.get(firebase_url + '/' + cardId + '.json', verify=False)
    try:
        cash = json.loads(result.text)['cash']
        print(cardId, cash)
        print('卡片 ' + cardId + ' 餘額 : ' + str(cash))
        balance = cash - fee
        if(balance >= 0):
            data = {'cash': balance}
            result = requests.put(firebase_url + '/' + cardId + '.json', verify=False, data=json.dumps(data))
            print('卡片 ' + cardId + ' 消費成功, 餘額 : ' + str(balance))
        else:
            print('卡片 ' + cardId + ' 消費失敗, 餘額 : ' + str(cash))
    except:
        print('找無此卡, 請先進入開卡作業')


def add():
    cardId = getCardId()
    result = requests.get(firebase_url + '/' + cardId + '.json', verify=False)
    try:
        cash = json.loads(result.text)['cash']
        print(cardId, cash)
        print('卡片 ' + cardId + ' 餘額 : ' + str(cash))
        new_cash = int(input('請輸入金額 : '))
        balance = cash + new_cash
        if(balance >= 0):
            data = {'cash': balance}
            result = requests.put(firebase_url + '/' + cardId + '.json', verify=False, data=json.dumps(data))
            print('卡片 ' + cardId + ' 加值成功, 餘額 : ' + str(balance))
        else:
            print('卡片 ' + cardId + ' 加值失敗, 餘額 : ' + str(cash))
    except:
        print('找無此卡, 請先進入開卡作業')


def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()


signal.signal(signal.SIGINT, end_read)
rdr = RFID()
util = rdr.util()
print("Starting")
while True:
    menu()
    n = int(input('請選擇 : '))
    if(n == 1):
        print('開卡作業:' , end=' ')
        create()
    elif (n == 2):
        print('讀卡作業:' , end=' ')
        read()
    elif (n == 3):
        print('消費作業:' , end=' ')
        consumer()
    elif (n == 4):
        print('加值作業:' , end=' ')
        add()
    elif (n == 5):
        break

    input('按下 enter 後繼續')
