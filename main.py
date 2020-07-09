import mqttHandler as mqtHand
import _thread
import machine

# Send temp or mvmt values depending on wake_reason
def send():
    if machine.wake_reason()[0] == 1:
        mqtHand.send_mvmt_value(True)
    else:
        mqtHand.send_temp_value()
    sleep()

# Go to deepsleep for 3 hours, but allow P22 (PIR sensor) to wake machine so it's able to send motion detected,
# otherwise wake up every third hour to send temp data.
def sleep():
    machine.pin_sleep_wakeup(['P22'], mode=machine.WAKEUP_ANY_HIGH, enable_pull=False)
    print("Deepsleep for 3 hours")
    machine.deepsleep(3 * 60 * 60 * 1000)

# Start thread to send data
_thread.start_new_thread(send, ())
