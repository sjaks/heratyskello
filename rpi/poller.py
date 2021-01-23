# Herätyskello poller
# This sould be executed as a cron job every minute
# requires /dev/mem access on RPi
#
# Depends on: sudo pip3 install RPi.GPIO

import requests
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


# Plays beeping sound
def beep():
        # Poll server for wake up call status
        res = requests.get(ENTRY).text
        i = 0
        while res == "true" and i < 300: # die after 5 minutes
                # Keep checking server status
                res = requests.get(ENTRY).text

                # Beep the buzzer until the server tells to stop
                GPIO.output(buzzer,GPIO.HIGH)
                sleep(0.5)
                GPIO.output(buzzer,GPIO.LOW)
                sleep(0.5)
                i += 1

        # Turn buzzer off
        GPIO.output(buzzer, GPIO.LOW)


beep()
