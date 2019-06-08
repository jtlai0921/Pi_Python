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

try:
  while True:
    for digit in range(4):
      if digit == 0 or digit == 2:
         GPIO.output(11, 0)
         GPIO.output(12, 0)
         GPIO.output(19, 0)
      else:
         GPIO.output(11, 1)
         GPIO.output(12, 1)
         GPIO.output(19, 1)

      GPIO.output(digits[digit], 1)
      time.sleep(0.001)
      GPIO.output(digits[digit], 0)
except KeyboardInterrupt:
  GPIO.cleanup()
