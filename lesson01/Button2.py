from gpiozero import Button
from time import sleep

button = Button(25) # GPIO(25), Board(22)

button.wait_for_press()
print('Pressed')

