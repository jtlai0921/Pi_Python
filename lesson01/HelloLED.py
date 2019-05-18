import time
import RPi.GPIO as GPIO

# 設定 GPIO 腳位模式
GPIO.setmode(GPIO.BOARD)

# 設定 LED pin變數
LED0 = 12

# 設定為輸出
GPIO.setup(LED0, GPIO.OUT)

# 開燈
GPIO.output(LED0, GPIO.HIGH)
print('開燈')

# 延遲 3 秒
time.sleep(3)

# 關燈
GPIO.output(LED0, GPIO.LOW)
print('關燈')
