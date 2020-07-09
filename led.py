import pycom
import time

# Blink pycom heartbeat in Color Greeen
def blink_led_green():
    pycom.heartbeat(False)
    pycom.rgbled(0xfcfc03)
    time.sleep(0.5)
    pycom.rgbled(0x000000)
    time.sleep(0.2)
