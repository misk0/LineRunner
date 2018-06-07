from RPi import GPIO
import config
import time
import Distance

def Rubble(debug):
    right_dist = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    # left_dist = round(Distance.measure_distance(config.US_LEFT)-1.8,1) #5.8cm ->4cm

    if config.RubbleCount == 10:
        config.RubblePrevRight = right_dist

    # print("right",right_dist)
    # print("left",left_dist)

    if config.RubblePrevRight - right_dist > 1.2:
        config.RubbleError = 4
        if debug:
            print("troppo sin")
    if config.RubblePrevRight - right_dist > 0.9 and config.RubblePrevRight - right_dist <= 1.2:
        config.RubbleError = 3
        if debug:
            print("quasitroppo sin")
    if config.RubblePrevRight - right_dist > 0.6 and config.RubblePrevRight - right_dist <= 0.9:
        config.RubbleError = 2
        if debug:
            print("unpopiu sin")
    if config.RubblePrevRight - right_dist > 0.3 and config.RubblePrevRight - right_dist <= 0.6:
        config.RubbleError = 1
        if debug:
            print("unpo sin")#gira destra
    if abs(right_dist - config.RubblePrevRight) <= 0.3:
        config.RubbleError = 0
        if debug:
            print("mid")
    if right_dist - config.RubblePrevRight > 0.3 and right_dist - config.RubblePrevRight <= 0.6:
        config.RubbleError = -1
        if debug:
            print("unpo dx")
    if right_dist - config.RubblePrevRight > 0.6 and right_dist - config.RubblePrevRight <= 0.9:
        config.RubbleError = -2
        if debug:
            print("unpopiu dx")
    if right_dist - config.RubblePrevRight > 0.9 and right_dist - config.RubblePrevRight  <= 1.2:
        config.RubbleError = -3
        if debug:
            print("quasitroppo dx")
    if right_dist - config.RubblePrevRight > 1.2:
        config.RubbleError = -4
        if debug:
            print("troppo dx")

    P = config.RubbleError
    # D = config.dist_error - config.dist_previous_error
    PIDvalue = (8 * P)
    # config.dist_previous_error = config.dist_error
    # print("PID", PIDvalue)

    if config.RubbleRightSpeed + PIDvalue > 100:
        config.walk_speed_right = 100
    elif config.RubbleRightSpeed + PIDvalue < 0:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.RubbleRightSpeed + PIDvalue

    if config.RubbleLeftSpeed - PIDvalue > 100:
        config.walk_speed_left = 100
    elif config.RubbleLeftSpeed - PIDvalue < 0:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.RubbleLeftSpeed - PIDvalue

    if config.RubbleCount < 5:
        config.RubbleCount = config.RubbleCount + 1
    else:
        config.RubblePrevRight = right_dist
        config.RubbleCount = 0
        # print("10 misure")

