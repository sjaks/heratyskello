# Herätyskello poller
# requires /dev/mem access on RPi
#
# Depends on: sudo pip3 install RPi.GPIO

import requests
import threading
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


# Define GPIO pin for buzzer (19-00012533)
# OUTER ROW: - - 0 - - - - 1 - - ...
# INNER ROW: - - - - - - - - - - ...
buzzer = 23
GPIO.setup(buzzer, GPIO.OUT)


# Define entry point to remote server
ENTRY = "https://jaks.fi/wakey/get"


# Test your local speaker system
# If you hear a sound everything works
def speakerTest():
    for i in range(0, 9):
        print("Beep number:", i+1)
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(buzzer, GPIO.LOW)
        sleep(0.5)
    print("Test ended. If you heard ten beeps your system is functioning.")

# Helper for periodical function calls
def setInterval(func, interval):
    ev = threading.Event()
    while not ev.wait(interval):
        func()


# Plays beeping sound
def beep():
        # Poll server for wake up call status
        res = requests.get(ENTRY).text
        print("Polling server: " + res)
        i = 0
        while res == "true" and i < 300: # die after 5 minutes
                # Keep checking server status
                res = requests.get(ENTRY).text

                # Beep the buzzer until the server tells to stop
                GPIO.output(buzzer, GPIO.HIGH)
                sleep(0.5)
                GPIO.output(buzzer, GPIO.LOW)
                sleep(0.5)
                print("---> beep")
                i += 1

        # Turn buzzer off
        GPIO.output(buzzer, GPIO.LOW)


# Prevent auto run on import
if __name__ == "__main__":
    setInterval(beep, 3)
