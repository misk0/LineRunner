import Distance
import config
from RPi import GPIO
import time
import signal
import sys


config.init()

GPIO.setmode(GPIO.BOARD)

#Distance sensors
#Left
GPIO.setup(config.ultrasonic_triggers[config.US_LEFT], GPIO.OUT)
GPIO.setup(config.ultrasonic_echo[config.US_LEFT], GPIO.IN)
#Mid
# GPIO.setup(config.ultrasonic_triggers[config.US_CENTER], GPIO.OUT)
# GPIO.setup(config.ultrasonic_echo[config.US_CENTER], GPIO.IN)
#Right
GPIO.setup(config.ultrasonic_triggers[config.US_RIGHT], GPIO.OUT)
GPIO.setup(config.ultrasonic_echo[config.US_RIGHT], GPIO.IN)

#Motor right
GPIO.setup(config.right_motor_pwm, GPIO.OUT)
GPIO.setup(config.right_motor_direction, GPIO.OUT)
GPIO.setup(config.right_motor_direction_inv, GPIO.OUT)

#Motor left
GPIO.setup(config.left_motor_pwm, GPIO.OUT)
GPIO.setup(config.left_motor_direction, GPIO.OUT)
GPIO.setup(config.left_motor_direction_inv, GPIO.OUT)

#Line sensors
GPIO.setup(config.line_follow_lmax, GPIO.IN)
GPIO.setup(config.line_follow_lmin, GPIO.IN)
GPIO.setup(config.line_follow_mid, GPIO.IN)
GPIO.setup(config.line_follow_rmin, GPIO.IN)
GPIO.setup(config.line_follow_rmax, GPIO.IN)

#Initialize motors
config.drive_left = GPIO.PWM(config.left_motor_pwm, 100)
config.drive_right = GPIO.PWM(config.right_motor_pwm, 100)

GPIO.output(config.left_motor_direction, GPIO.HIGH)
GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
GPIO.output(config.right_motor_direction, GPIO.HIGH)
GPIO.output(config.right_motor_direction_inv, GPIO.LOW)


def end_read(signal, frame):
    print("\nCtrl+C captured, ending read.")
    config.drive_left.stop()
    config.drive_right.stop()
    GPIO.cleanup()
    sys.exit()


def loop(debug=False):
    #desired distance from left wall = 10cm
    dist_right = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    dist_left = round(Distance.measure_distance(config.US_LEFT)-1.8,1)
    print("right",dist_right)
    print("left",dist_left)

    if dist_left-dist_right >10:
        config.line_error = 4
        if debug:
            print("troppo sin")
    elif dist_left-dist_right >8:
        config.line_error = 3
        if debug:
            print("quasitroppo sin")
    elif dist_left-dist_right >6:
        config.line_error = 2
        if debug:
            print("unpopiu sin")
    elif dist_left-dist_right >2:
        config.line_error = 1
        if debug:
            print("unpo sin")
    elif dist_left-dist_right == 0:
        config.line_error = 0
        if debug:
            print("mid")
    elif dist_right-dist_left > 10:
        config.line_error = -4
        if debug:
            print("troppo dx")
    elif dist_right-dist_left > 8:
        config.line_error = -3
        if debug:
            print("quasitroppo sx")
    elif dist_right-dist_left > 6:
        config.line_error = -2
        if debug:
            print("unpopiu dx")
    elif dist_right-dist_left > 2:
        config.line_error = -1
        if debug:
            print("unpo dx")




    P = config.line_error
    D = config.line_error - config.previous_error
    PIDvalue = (5 * P) + (0 * D)
    print("PID",PIDvalue)

    if 45 - PIDvalue > 100:
        config.walk_speed_left = 100
    elif 45 - PIDvalue < config.min_left_speed:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = 45 - PIDvalue

    if 45 + PIDvalue > 100:
        config.walk_speed_right = 100
    elif 45 + PIDvalue < config.min_right_speed:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = 45 + PIDvalue

    config.previous_error = config.line_error


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_read)

config.walk_speed_left = 50
config.walk_speed_right = 50
config.drive_left.start(config.walk_speed_left)
config.drive_right.start(config.walk_speed_right)

while True:
    loop(debug=False)
    config.drive_left.ChangeDutyCycle(config.walk_speed_left)
    print("speed left",config.walk_speed_left)
    config.drive_right.ChangeDutyCycle(config.walk_speed_right)
    print("speed right", config.walk_speed_right)