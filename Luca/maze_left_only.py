import Distance
import config
from RPi import GPIO
import time
import signal
import sys


config.init()

GPIO.setmode(GPIO.BOARD)

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
GPIO.setup(config.ultrasonic_echo[config.US_LEFT], GPIO.IN)
GPIO.setup(config.ultrasonic_echo[config.US_CENTER], GPIO.IN)
GPIO.setup(config.ultrasonic_echo[config.US_RIGHT], GPIO.IN)

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
    dist_mid = Distance.measure_distance(config.US_CENTER)
    dist_left = Distance.measure_distance(config.US_LEFT)
    dist_right = Distance.measure_distance(config.US_RIGHT)
    print("left", dist_left)
    print("mid", dist_mid)
    print("right", dist_right)

    if dist_mid <= 8:
        config.drive_left.ChangeDutyCycle(0)
        config.drive_right.ChangeDutyCycle(0)
        GPIO.output(config.left_motor_direction, GPIO.HIGH)
        GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
        GPIO.output(config.right_motor_direction, GPIO.LOW)
        GPIO.output(config.right_motor_direction_inv, GPIO.HIGH)
        config.drive_left.ChangeDutyCycle(78)
        config.drive_right.ChangeDutyCycle(78)
        time.sleep(0.705)  # time needed to turn 90° right
        config.drive_left.ChangeDutyCycle(0)
        config.drive_right.ChangeDutyCycle(0)
        GPIO.output(config.left_motor_direction, GPIO.HIGH)
        GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
        GPIO.output(config.right_motor_direction, GPIO.HIGH)
        GPIO.output(config.right_motor_direction_inv, GPIO.LOW)
    else:
        debug = False
        if dist_left < 7:
            config.line_error = 4
            if debug:
                print("troppo sin")
        if dist_left == 7:
            config.line_error = 3
            if debug:
                print("quasitroppo sin")
        if dist_left == 8:
            config.line_error = 2
            if debug:
                print("unpopiu sin")
        if dist_left == 9:
            config.line_error = 1
            if debug:
                print("unpo sin")
        if dist_left == 10:
            config.line_error = 0
            if debug:
                print("mid")
        if dist_left == 13:
            config.line_error = -1
            if debug:
                print("unpo dx")
        if dist_left == 14:
            config.line_error = -2
            if debug:
                print("unpopiu dx")
        if dist_left == 15:
            config.line_error = -3
            if debug:
                print("quasitroppo sx")
        if dist_left > 15:
            config.line_error = -4
            if debug:
                print("troppo dx")

        P = config.line_error
        D = config.line_error - config.previous_error
        PIDvalue = (8 * P)

        if 60 - PIDvalue > 100:
            config.walk_speed_right = 100
        elif 60 - PIDvalue < config.min_right_speed:
            config.walk_speed_right = 0
        else:
            config.walk_speed_right = config.line_right_speed - PIDvalue

        if 58 + PIDvalue > 100:
            config.walk_speed_left = 100
        elif 58 + PIDvalue < config.min_left_speed:
            config.walk_speed_left = 0
        else:
            config.walk_speed_left = config.line_left_speed + PIDvalue

        config.previous_error = config.line_error


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_read)
config.walk_speed_left = 60
config.walk_speed_right = 60
config.drive_left.start(config.walk_speed_left)
config.drive_right.start(config.walk_speed_right)

while True:
    loop(debu=False)
    config.drive_left.ChangeDutyCycle(config.walk_speed_left)
    config.drive_right.ChangeDutyCycle(config.walk_speed_right)
    time.sleep(0.2)
    config.drive_left.ChangeDutyCycle(0)
    config.drive_right.ChangeDutyCycle(0)

