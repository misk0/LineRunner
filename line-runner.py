from config import *
from RPi import GPIO
from threading import Thread
import time
import RFIDReader
from gpiozero import  PWMOutputDevice


def line_follow(self):
    do_something = True


# Create thread for RFID reading
rfid = RFIDReader.RFIDReader()
rfidThread = Thread(target=rfid.run)
rfidThread.start()

# Create thread for line following
counter = 0

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
driveLeft = PWMOutputDevice(left_motor_pwm, True, 0, 1000)
driveRight = PWMOutputDevice(right_motor_pwm, True, 0, 1000)
# Initialise objects for H-Bridge digital GPIO pins
forwardLeft = PWMOutputDevice(left_motor_direction)
forwardRight = PWMOutputDevice(right_motor_direction)

while walk_running:
    counter += 1
    if counter == 20:
        walk_running = False
    print("Line {}".format(counter))
    time.sleep(0.5)

    forwardLeft.value = True
    forwardRight.value = True
    driveLeft.value = 1.0
    driveRight.value = 1.0

    #OldRange = -90 -> 90
    #NewRange =
    #NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
    #coef = (MAX_SPEED / 2 ) / 90
    #left_tracker_speed = (MAX_SPEED / 2) + walk_angle * 2.5
    #right_tracker_speed = (MAX_SPEED / 2) - walk_angle * 2.5


    # Automatic walk: Robot does not stop nor count distance. It's possible to change speed and direction
    #while walk_running and walk_mode_automatic:
    #    walk_angle = walk_speed_left / walk_speed_right
    #    run = 1

    # Manual walk: Robot moves only while certain distance is not reached
    #while walk_running and not walk_mode_automatic:
    #    run = 2
print(obstacle_number)
rfid.terminate()
driveLeft.close()
driveRight.close()
forwardLeft.close()
forwardRight.close()
