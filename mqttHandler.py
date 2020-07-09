from mqtt import MQTTClient
import led
import ubinascii
import hashlib
import json
import time
import read_dht
import machine

topic_pub = 'home/groundFloor'
broker_url = 'broker.hivemq.com'
client_name = ubinascii.hexlify(hashlib.md5(machine.unique_id()).digest()) # create a md5 hash of the pycom WLAN mac

client = MQTTClient(client_name, broker_url, port=1883)
client.connect()

# Get and send temp values to publisher
def send_temp_value():
    topic = topic_pub + "/temp"
    try:
        dht_T, dht_RH = read_dht.value()
        print('dht temp: ', dht_T)
        print('dht RH: ', dht_RH)

        sensorData = {
              "groundFloorTempAndHumi":{
                "dht temp": dht_T,
                "dht RH": dht_RH
                }
            }
        publish_sensor_value(topic, sensorData)
    except Exception as e:
        print("Failed to read temp data")

# Send mvmt values to publisher
def send_mvmt_value(movement):
    topic = topic_pub + "/mvmt"
    print('Movement: ', int(movement))

    sensorData = {
          "groundFloorMovement":{
            "Movement": int(movement)
            }
        }

    publish_sensor_value(topic, sensorData)
    time.sleep(5)

# Publish sensor data to topic
def publish_sensor_value(topic, sensorData):
    client.connect()
    try:
        client.publish(topic,json.dumps(sensorData))
        print('Sensor data sent ..')
        client.disconnect()
        led.blink_led_green()

    except(NameError, ValueError, TypeError) as e:
        print("Fail to send data!")
        print(e)
