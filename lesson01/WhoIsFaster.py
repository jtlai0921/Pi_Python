from gpiozero import LED
from gpiozero import Button
from gpiozero import Buzzer
import random
import time

green_btn = Button(18)
green_led1 = LED(24)
green_led2 = LED(23)

yellow_btn = Button(25)
yellow_led1 = LED(20)
yellow_led2 = LED(21)

red = LED(12)
buzzer = Buzzer(16)

green_count = 0
yellow_count = 0

buzzer.beep(0.4, 0.4, 1, False)
buzzer.beep(0.4, 0.4, 1, False)
buzzer.beep(0.4, 0.4, 1, False)
while not (green_count == 2 or yellow_count == 2):
    red.off()
    buzzer.beep(1, 0.4, 1, False)
    ts = random.randint(2, 10)
    time.sleep(ts)
    red.on()
    while True:
        if green_btn.is_pressed:
            print('green win')
            green_count = green_count + 1
            if green_count == 1:
                green_led1.on()
            else:
                green_led2.on()
            break
        if yellow_btn.is_pressed:
            print('yellow win')
            yellow_count = yellow_count + 1
            if yellow_count == 1:
                yellow_led1.on()
            else:
                yellow_led2.on()
            break
    time.sleep(0.5)

print('game over')
buzzer.beep(0.1, 0.1, 10, False)
time.sleep(2)