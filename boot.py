from network import WLAN
import machine
import json
wlan = WLAN(mode=WLAN.STA)

# Open config file
with open('secrets/config.json') as f:
    config = json.load(f)

# Connect to WiFi
nets = wlan.scan()
for net in nets:
    if net.ssid == config['SSID']:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, config['SSID_PASS']), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
