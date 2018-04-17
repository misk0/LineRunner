from config import *
from RPi import GPIO


# Create callback event which will be triggered when RFID read something
GPIO.add_event_detect()


while walk_running:
    # run motors

    # Automatic walk: Robot does not stop nor count distance. It's possible to change speed and direction
    while walk_running and walk_mode_automatic:
        run = 1

    # Manual walk: Robot moves only while certain distance is not reached
    while walk_running and not walk_mode_automatic:
        run = 2
