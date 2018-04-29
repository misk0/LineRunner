import config
from RPi import GPIO
from threading import Thread
from gpiozero import PWMOutputDevice
import time
import RFIDReader
import FollowMeBaby

config.init()

def line_follow(self):
    do_something = True


# Create thread for RFID reading
rfid = RFIDReader.RFIDReader()
rfidThread = Thread(target=rfid.run)
rfidThread.start()

# Create thread for line following
# follower = FollowMeBaby.FollowMeBaby()
# followerThread = Thread(target=follower.run)
# followerThread.start()


counter = 0

# Initialise objects for H-Bridge GPIO PWM pins
# Set initial duty cycle to 0 and frequency to 1000
# driveLeft = PWMOutputDevice(config.left_motor_pwm, True, 0, 1000)
# driveRight = PWMOutputDevice(config.right_motor_pwm, True, 0, 1000)
# Initialise objects for H-Bridge digital GPIO pins
# forwardLeft = PWMOutputDevice(config.left_motor_direction)
# forwardRight = PWMOutputDevice(config.right_motor_direction)

while config.walk_running:
    counter += 1
    if counter == 20:
        config.walk_running = False
    print("Line {}".format(counter))
    time.sleep(0.5)

    # forwardLeft.value = True
    # forwardRight.value = True
    # driveLeft.value = config.walk_speed_left
    # driveRight.value = config.walk_speed_right

    # Automatic walk: Robot does not stop nor count distance. It's possible to change speed and direction
    #while walk_running and walk_mode_automatic:
    #    walk_angle = walk_speed_left / walk_speed_right
    #    run = 1

    # Manual walk: Robot moves only while certain distance is not reached
    #while walk_running and not walk_mode_automatic:
    #    run = 2

print(config.obstacle_number)
rfid.terminate()
follower.terminate()

# driveLeft.close()
# driveRight.close()
# forwardLeft.close()
# forwardRight.close()
