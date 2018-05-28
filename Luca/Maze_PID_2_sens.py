import Distance
import config
from RPi import GPIO
import time
import signal
import sys


config.init()

GPIO.setup(config.left_motor_pwm, GPIO.OUT)
GPIO.setup(config.left_motor_direction, GPIO.OUT)
GPIO.setup(config.left_motor_direction_inv, GPIO.OUT)
GPIO.setup(config.right_motor_pwm, GPIO.OUT)
GPIO.setup(config.right_motor_direction, GPIO.OUT)
GPIO.setup(config.right_motor_direction_inv, GPIO.OUT)

config.drive_left = GPIO.PWM(config.left_motor_pwm, 100)
config.drive_right = GPIO.PWM(config.right_motor_pwm, 100)

GPIO.setup(config.ultrasonic_triggers[config.US_LEFT], GPIO.OUT)
GPIO.setup(config.ultrasonic_triggers[config.US_CENTER], GPIO.OUT)
GPIO.setup(config.ultrasonic_triggers[config.US_RIGHT], GPIO.OUT)
GPIO.setup(config.ultrasonic_pins[config.US_LEFT], GPIO.IN)
GPIO.setup(config.ultrasonic_pins[config.US_CENTER], GPIO.IN)
GPIO.setup(config.ultrasonic_pins[config.US_RIGHT], GPIO.IN)

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


def loop(debu=False):
    #desired distance from left wall = 10cm
    dist_left = Distance.measure_distance(config.ultrasonic_triggers[config.US_LEFT], debug=False)
    dist_right = Distance.measure_distance(config.ultrasonic_triggers[config.US_RIGHT], debug=False)

    if dist_left-dist_right >8:
        config.line_error = 4
        if debug:
            print("troppo sin")
    elif dist_left-dist_right >6:
        config.line_error = 3
        if debug:
            print("quasitroppo sin")
    elif dist_left-dist_right >4:
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
    elif dist_right-dist_left > 8:
        config.line_error = -4
        if debug:
            print("troppo dx")
    elif dist_right-dist_left > 6:
        config.line_error = -3
        if debug:
            print("quasitroppo sx")
    elif dist_right-dist_left > 4:
        config.line_error = -2
        if debug:
            print("unpopiu dx")
    elif dist_right-dist_left > 2:
        config.line_error = -1
        if debug:
            print("unpo dx")




    P = config.line_error
    D = config.line_error - config.previous_error
    PIDvalue = (15 * P) + (20 * D)

    if 60 - PIDvalue > 100:
        config.walk_speed_left = 100
    elif 60 - PIDvalue < config.min_left_speed:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.line_left_speed - PIDvalue

    if 58 + PIDvalue > 100:
        config.walk_speed_right = 100
    elif 58 + PIDvalue < config.min_right_speed:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.line_right_speed + PIDvalue

    config.previous_error = config.line_error


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_read)

config.drive_left.start(config.walk_speed_left)
config.drive_right.start(config.walk_speed_right)

while True:
    loop(debu=False)
    config.drive_left.ChangeDutyCycle(config.walk_speed_left)
    config.drive_right.ChangeDutyCycle(config.walk_speed_right)
