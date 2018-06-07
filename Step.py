from RPi import GPIO
import config
import time
import Distance

def Step(debug):
    right_dist = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    # left_dist = round(Distance.measure_distance(config.US_LEFT)-1.8,1) #5.8cm ->4cm

    if config.StepCount == 10:
        config.StepPrevRight = right_dist

    # print("right",right_dist)
    # print("left",left_dist)

    if config.StepPrevRight - right_dist > 1.2:
        config.StepError = 4
        if debug:
            print("troppo sin")
    if config.StepPrevRight - right_dist > 0.9 and config.StepPrevRight - right_dist <= 1.2:
        config.StepError = 3
        if debug:
            print("quasitroppo sin")
    if config.StepPrevRight - right_dist > 0.6 and config.StepPrevRight - right_dist <= 0.9:
        config.StepError = 2
        if debug:
            print("unpopiu sin")
    if config.StepPrevRight - right_dist > 0.3 and config.StepPrevRight - right_dist <= 0.6:
        config.StepError = 1
        if debug:
            print("unpo sin")#gira destra
    if abs(right_dist - config.StepPrevRight) <= 0.3:
        config.StepError = 0
        if debug:
            print("mid")
    if right_dist - config.StepPrevRight > 0.3 and right_dist - config.StepPrevRight <= 0.6:
        config.StepError = -1
        if debug:
            print("unpo dx")
    if right_dist - config.StepPrevRight > 0.6 and right_dist - config.StepPrevRight <= 0.9:
        config.StepError = -2
        if debug:
            print("unpopiu dx")
    if right_dist - config.StepPrevRight > 0.9 and right_dist - config.StepPrevRight  <= 1.2:
        config.StepError = -3
        if debug:
            print("quasitroppo dx")
    if right_dist - config.StepPrevRight > 1.2:
        config.StepError = -4
        if debug:
            print("troppo dx")

    P = config.StepError
    # D = config.dist_error - config.dist_previous_error
    PIDvalue = (8 * P)
    # config.dist_previous_error = config.dist_error
    # print("PID", PIDvalue)

    if config.StepRightSpeed + PIDvalue > 100:
        config.walk_speed_right = 100
    elif config.StepRightSpeed + PIDvalue < 0:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.StepRightSpeed + PIDvalue

    if config.StepLeftSpeed - PIDvalue > 100:
        config.walk_speed_left = 100
    elif config.StepLeftSpeed - PIDvalue < 0:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.StepLeftSpeed - PIDvalue

    if config.StepCount < 5:
        config.StepCount = config.StepCount + 1
    else:
        config.StepPrevRight = right_dist
        config.StepCount = 0
        # print("10 misure")

