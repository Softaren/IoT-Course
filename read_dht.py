from dht import DTH
from machine import Pin
import time

# Read the dht_11 sensor values and return temperature and humidity
def value():
    th = DTH(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
    time.sleep(3)
    result = th.read()
    if result.is_valid():
        return(result.temperature,result.humidity)
