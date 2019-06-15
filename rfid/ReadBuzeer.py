#!/usr/bin/env python

import signal
import time
import sys

import RPi.GPIO as GPIO

from pirc522 import RFID

GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
buzeer = GPIO.PWM(32, 50) # GPIO.PWM(channel, frequency)

run = True
rdr = RFID()
util = rdr.util()
util.debug = True


def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    run = False
    rdr.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)

print("Starting")
while run:
    rdr.wait_for_tag()
    (error, data) = rdr.request()
    if error:
        print("Read Error")

    (error, uid) = rdr.anticoll()
    if not error:
        cardId = str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
        print("Card read UID: " + cardId)

        buzeer.ChangeFrequency(1) # set frequency
        buzeer.start(10)  # 占空比 (0.0 <= dc <= 100.0)
        time.sleep(0.1) # for buzeer
        buzeer.stop()

        time.sleep(1) # for rfid card


GPIO.cleanup()