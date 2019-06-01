from gpiozero import MCP3008
from time import sleep
from RPLCD.i2c import CharLCD

lm35 = MCP3008(channel=1)
lcd = CharLCD('PCF8574', address=0x3f, port=1, backlight_enabled=True)
lcd.clear()

def convert_temp(gen):
    for value in gen:
        print('value=', value)
        yield value * 3.3 * 100


for temp in convert_temp(lm35.values):
    print('The temp is ', temp, ' C')
    lcd.cursor_pos = (0, 0)
    lcd.write_string('Temp %.2f C' % temp)
    sleep(1)
