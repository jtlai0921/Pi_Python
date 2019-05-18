from gpiozero import Button
from time import sleep

button = Button(25) # GPIO(25), Board(22)

while True:
    if button.is_pressed:
        print('Pressed')

    sleep(0.1)

