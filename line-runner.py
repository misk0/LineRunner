from config import *
from RPi import GPIO
import threading

def line_follow(self):
    do_something = True

def read_rfid(self):
    something_else = True



# Create thread event which will be triggered when RFID read something

# Create thread for line following

while walk_running:
    # run motors

    # Automatic walk: Robot does not stop nor count distance. It's possible to change speed and direction
    while walk_running and walk_mode_automatic:
        walk_angle = walk_speed_left / walk_speed_right
        run = 1

    # Manual walk: Robot moves only while certain distance is not reached
    while walk_running and not walk_mode_automatic:
        run = 2
