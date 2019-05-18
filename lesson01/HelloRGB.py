import time
import RPi.GPIO as GPIO

# 設定 GPIO 腳位模式
GPIO.setmode(GPIO.BOARD)

# 關閉警告
GPIO.setwarnings(False)

# 設定 LED pin變數
LED0 = 11 #R
LED1 = 13 #G
LED2 = 15 #B

# 設定為輸出
GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

# RGB 輪詢
GPIO.output(LED0, GPIO.HIGH)
GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)
print("R")
time.sleep(2)

GPIO.output(LED0, GPIO.LOW)
GPIO.output(LED1, GPIO.HIGH)
GPIO.output(LED2, GPIO.LOW)
print("G")
time.sleep(2)

GPIO.output(LED0, GPIO.LOW)
GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.HIGH)
print("B")
time.sleep(2)

GPIO.output(LED0, GPIO.LOW)
GPIO.output(LED1, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)
print("End")