from config import *
from RPi import GPIO
from threading import Thread
import time
import RFIDReader


def line_follow(self):
    do_something = True

def read_rfid(self):
    something_else = True


# Create thread for RFID reading
rfid = RFIDReader.RFIDReader()
rfidThread = Thread(target=rfid.run)
rfidThread.start()

# Create thread for line following
counter = 0

while walk_running:
    counter += 1
    if counter == 20:
        walk_running = False
    print("Line {}".format(counter))
    time.sleep(0.5)


    # Automatic walk: Robot does not stop nor count distance. It's possible to change speed and direction
    #while walk_running and walk_mode_automatic:
    #    walk_angle = walk_speed_left / walk_speed_right
    #    run = 1

    # Manual walk: Robot moves only while certain distance is not reached
    #while walk_running and not walk_mode_automatic:
    #    run = 2
rfid.terminate()
