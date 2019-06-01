from gpiozero import MCP3008
from time import sleep

cds = MCP3008(channel=5)

while True:
    print(cds.value)
    sleep(1)


