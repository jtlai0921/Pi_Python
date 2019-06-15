import pymysql

import time
import RPi.GPIO as GPIO
from pirc522 import RFID

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
buzeer = GPIO.PWM(32, 50) # GPIO.PWM(channel, frequency)

run = True
rdr = RFID()
util = rdr.util()
util.debug = True

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

def insert(uids):
    conn = pymysql.connect(host= "localhost",
                          user="remote",
                          passwd="1234",
                          db="pi")
    x = conn.cursor()
    x.execute("INSERT INTO RFID_Log(uids, cost) VALUES ('%s', 0)" % uids)
    print('ok')
    conn.commit()
    conn.close()

while True:
    insert(getCardId())
    time.sleep(1)