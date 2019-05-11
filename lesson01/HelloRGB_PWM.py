# https://wp.huangshiyang.com/pwm%E4%BD%BF%E7%94%A8-rpi-gpio-%E6%A8%A1%E5%9D%97%E7%9A%84%E8%84%89%E5%AE%BD%E8%B0%83%E5%88%B6
import time
import RPi.GPIO as GPIO
import random


def setColor(r, g, b, ts):
    red_pwm.ChangeDutyCycle(r * 100 / 255)
    blue_pwm.ChangeDutyCycle(g * 100 / 255)
    green_pwm.ChangeDutyCycle(b * 100 / 255)
    time.sleep(ts)

# 設定 GPIO 腳位模式
GPIO.setmode(GPIO.BOARD)

# 關閉警告
GPIO.setwarnings(False)

# 設定 LED pin變數
LED0 = 11
LED1 = 13
LED2 = 15
PWM_FREQ = 200

# 設定為輸出
GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

red_pwm = GPIO.PWM(LED0, PWM_FREQ)
red_pwm.start(0)
blue_pwm = GPIO.PWM(LED1, PWM_FREQ)
blue_pwm.start(0)
green_pwm = GPIO.PWM(LED2, PWM_FREQ)
green_pwm.start(0)

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    setColor(r, g, b, 0.5)

red_pwm.stop()
blue_pwm.stop()
green_pwm.stop()
GPIO.cleanup()
print("End")