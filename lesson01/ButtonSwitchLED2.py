from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause

button = Button(25) # GPIO(25), Board(22)
green = LED(18)
yellow = LED(23)
red = LED(24)

count = 0

def switchLED() :
    global count
    count = (count + 1) % 5
    print('count=' + str(count))
    if count == 1:
        green.on()
        yellow.off()
        red.off()
    elif count == 2:
        green.off()
        yellow.on()
        red.off()
    elif count == 3:
        green.off()
        yellow.off()
        red.on()
    elif count == 4:
        green.on()
        yellow.on()
        red.on()
    elif count == 0:
        green.off()
        yellow.off()
        red.off()

button.when_pressed= switchLED
pause()