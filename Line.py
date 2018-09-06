from RPi import GPIO
import config
import time

def follow_line(debug):
    left_max_value = GPIO.input(config.line_follow_lmax)
    left_min_value = GPIO.input(config.line_follow_lmin)
    middle_value = GPIO.input(config.line_follow_mid)
    right_min_value = GPIO.input(config.line_follow_rmin)
    right_max_value = GPIO.input(config.line_follow_rmax)
    # print("left_max",left_max_value)
    # print("left_min", left_min_value)
    # print("mid", middle_value)
    # print("right_min", right_min_value)
    # print("right_max", right_max_value)

    if left_max_value == 0 and left_min_value == 0 and middle_value == 0 and right_min_value == 0 and right_max_value == 1:
        config.line_error = -4
    elif left_max_value == 0 and left_min_value == 0 and middle_value == 1 and right_min_value == 1 and right_max_value == 1:
        config.line_error = -4
    elif left_max_value == 0 and left_min_value == 1 and middle_value == 1 and right_min_value == 1 and right_max_value == 1:
        config.line_error = -4
        # config.drive_left.ChangeDutyCycle(0)
        # config.drive_right.ChangeDutyCycle(0)
        # GPIO.output(config.left_motor_direction, GPIO.HIGH)
        # GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
        # GPIO.output(config.right_motor_direction, GPIO.LOW)
        # GPIO.output(config.right_motor_direction_inv, GPIO.HIGH)
        # config.drive_left.ChangeDutyCycle(78)
        # config.drive_right.ChangeDutyCycle(78)
        # time.sleep(0.3)  # time needed to turn 90° right
        # config.drive_left.ChangeDutyCycle(0)
        # config.drive_right.ChangeDutyCycle(0)
        # GPIO.output(config.left_motor_direction, GPIO.HIGH)
        # GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
        # GPIO.output(config.right_motor_direction, GPIO.HIGH)
        # GPIO.output(config.right_motor_direction_inv, GPIO.LOW)
        if debug:
            print("troppo sin")
    elif left_max_value == 0 and left_min_value == 0 and middle_value == 0 and right_min_value == 1 and right_max_value == 1:
        config.line_error = -3
        if debug:
            print("quasitroppo sin")
    elif left_max_value == 0 and left_min_value == 0 and middle_value == 0 and right_min_value == 1 and right_max_value == 0:
        config.line_error = -2
        if debug:
            print("unpopiu sin")
    elif left_max_value == 0 and left_min_value == 0 and middle_value == 1 and right_min_value == 1 and right_max_value == 0:
        config.line_error = -1
        if debug:
            print("unpo sin")
    elif left_max_value == 0 and left_min_value == 0 and middle_value == 1 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 0
        if debug:
            print("mid")
    elif left_max_value == 0 and left_min_value == 1 and middle_value == 1 and right_min_value == 1 and right_max_value == 0:
        config.line_error = 0
        if debug:
            print("mid")
    elif left_max_value == 0 and left_min_value == 1 and middle_value == 1 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 1
        if debug:
            print("unpo dx")
    elif left_max_value == 0 and left_min_value == 1 and middle_value == 0 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 2
        if debug:
            print("unpopiu dx")
    elif left_max_value == 1 and left_min_value == 1 and middle_value == 0 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 3
        if debug:
            print("quasitroppo sx")
    elif left_max_value == 1 and left_min_value == 0 and middle_value == 0 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 4
        if debug:
            print("troppo dx")
    elif left_max_value == 1 and left_min_value == 1 and middle_value == 1 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 4
    elif left_max_value == 1 and left_min_value == 1 and middle_value == 1 and right_min_value == 1 and right_max_value == 0:
        config.line_error = 4
    elif left_max_value == 1 and left_min_value == 1 and middle_value == 1 and right_min_value == 1 and right_max_value == 1:
        config.line_error = 0

    P = config.line_error
    # config.line_integrative = config.line_integrative + config.line_error
    D = config.line_error - config.previous_error
    PIDvalue = (config.line_kp * P) + (config.line_kd * D)

    if config.line_left_speed - PIDvalue > 100:
        config.walk_speed_left = 100
    elif config.line_left_speed - PIDvalue < config.min_left_speed: #config.min_left_speed
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.line_left_speed - PIDvalue

    if config.line_right_speed + PIDvalue > 100:
        config.walk_speed_right = 100
    elif config.line_right_speed + PIDvalue < config.min_right_speed: #config.min_right_speed
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.line_right_speed + PIDvalue

    config.previous_error = config.line_error
    # time.sleep(0.001)