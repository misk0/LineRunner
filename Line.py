from RPi import GPIO
import config
import time

def follow_line(debug):
    left_max_value = GPIO.input(config.line_follow_lmax)
    left_min_value = GPIO.input(config.line_follow_lmin)
    middle_value = GPIO.input(config.line_follow_mid)
    right_min_value = GPIO.input(config.line_follow_rmin)
    right_max_value = GPIO.input(config.line_follow_rmax)
    if left_max_value == 0 and left_min_value == 0 and middle_value == 0 and right_min_value == 0 and right_max_value == 1:
        config.line_error = -4
        if debug:
            print("troppo sin")
    if left_max_value == 0 and left_min_value == 0 and middle_value == 0 and right_min_value == 1 and right_max_value == 1:
        config.line_error = -3
        if debug:
            print("quasitroppo sin")
    if left_max_value == 0 and left_min_value == 0 and middle_value == 0 and right_min_value == 1 and right_max_value == 0:
        config.line_error = -2
        if debug:
            print("unpopiu sin")
    if left_max_value == 0 and left_min_value == 0 and middle_value == 1 and right_min_value == 1 and right_max_value == 0:
        config.line_error = -1
        if debug:
            print("unpo sin")
    if left_max_value == 0 and left_min_value == 0 and middle_value == 1 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 0
        if debug:
            print("mid")
    if left_max_value == 0 and left_min_value == 1 and middle_value == 1 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 1
        if debug:
            print("unpo dx")
    if left_max_value == 0 and left_min_value == 1 and middle_value == 0 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 2
        if debug:
            print("unpopiu dx")
    if left_max_value == 1 and left_min_value == 1 and middle_value == 0 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 3
        if debug:
            print("quasitroppo sx")
    if left_max_value == 1 and left_min_value == 0 and middle_value == 0 and right_min_value == 0 and right_max_value == 0:
        config.line_error = 4
        if debug:
            print("troppo dx")

    P = config.line_error
    # config.line_integrative = config.line_integrative + config.line_error
    D = config.line_error - config.previous_error
    PIDvalue = (config.line_kp * P) + (config.line_kd * D)

    if config.line_left_speed - PIDvalue > 100:
        config.walk_speed_left = 100
    elif config.line_left_speed - PIDvalue < config.min_left_speed:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.line_left_speed - PIDvalue

    if config.line_right_speed + PIDvalue > 100:
        config.walk_speed_right = 100
    elif config.line_right_speed + PIDvalue < config.min_right_speed:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.line_right_speed + PIDvalue

    config.previous_error = config.line_error
    # time.sleep(0.001)