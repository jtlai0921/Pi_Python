from gpiozero import MCP3008
from time import sleep
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', address=0x3f, port=1, backlight_enabled=True)

pot = MCP3008(0)
lcd.clear()
while True:
    print(pot.value)
    lcd.cursor_pos = (0, 0)
    lcd.write_string(str(pot.value))
    sleep(0.5)
