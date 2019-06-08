import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

segments = (24,12,19,21,23,22,15,11)

for segment in segments:
  GPIO.setup(segment, GPIO.OUT)
  GPIO.output(segment, 1)

digits = (26,18,16,13)
for digit in digits:
  GPIO.setup(digit, GPIO.OUT)
  GPIO.output(digit, 1)

num = {' ':(1,1,1,1,1,1,1),
'0':(0,0,0,0,0,0,1),
'1':(1,0,0,1,1,1,1),
'2':(0,0,1,0,0,1,0),
'3':(0,0,0,0,1,1,0),
'4':(1,0,0,1,1,0,0),
'5':(0,1,0,0,1,0,0),
'6':(0,1,0,0,0,0,0),
'7':(0,0,0,1,1,1,1),
'8':(0,0,0,0,0,0,0),
'9':(0,0,0,0,1,0,0)}

try:
  while True:
    n = time.ctime()[11:13]+time.ctime()[14:16]
    s = str(n).rjust(4)
    for digit in range(4):
      for loop in range(0,7):
        GPIO.output(segments[loop], num[s[digit]][loop])
        #print(segments[loop], num[s[digit]][loop])
        if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
          GPIO.output(11, 0)
        else:
          GPIO.output(11, 1)

      GPIO.output(digits[digit], 1)
      #print(digits[digit], 1)
      time.sleep(0.001)
      GPIO.output(digits[digit], 0)
      #print(digits[digit], 0)
except KeyboardInterrupt:
  GPIO.cleanup()
