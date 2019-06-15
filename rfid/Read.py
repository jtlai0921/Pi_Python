#!/usr/bin/env python

import signal
import time
import sys

from pirc522 import RFID

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
        time.sleep(1)
