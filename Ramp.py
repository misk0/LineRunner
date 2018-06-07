from RPi import GPIO
import config
import time
import Distance

def Ramp(debug):
    right_dist = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    # left_dist = round(Distance.measure_distance(config.US_LEFT)-1.8,1) #5.8cm ->4cm

    if config.RampCount == 10:
        config.RampPrevRight = right_dist

    # print("right",right_dist)
    # print("left",left_dist)

    if config.RampPrevRight - right_dist > 1.2:
        config.RampError = 4
        if debug:
            print("troppo sin")
    if config.RampPrevRight - right_dist > 0.9 and config.RampPrevRight - right_dist <= 1.2:
        config.RampError = 3
        if debug:
            print("quasitroppo sin")
    if config.RampPrevRight - right_dist > 0.6 and config.RampPrevRight - right_dist <= 0.9:
        config.RampError = 2
        if debug:
            print("unpopiu sin")
    if config.RampPrevRight - right_dist > 0.3 and config.RampPrevRight - right_dist <= 0.6:
        config.RampError = 1
        if debug:
            print("unpo sin")#gira destra
    if abs(right_dist - config.RampPrevRight) <= 0.3:
        config.RampError = 0
        if debug:
            print("mid")
    if right_dist - config.RampPrevRight > 0.3 and right_dist - config.RampPrevRight <= 0.6:
        config.RampError = -1
        if debug:
            print("unpo dx")
    if right_dist - config.RampPrevRight > 0.6 and right_dist - config.RampPrevRight <= 0.9:
        config.RampError = -2
        if debug:
            print("unpopiu dx")
    if right_dist - config.RampPrevRight > 0.9 and right_dist - config.RampPrevRight  <= 1.2:
        config.RampError = -3
        if debug:
            print("quasitroppo dx")
    if right_dist - config.RampPrevRight > 1.2:
        config.RampError = -4
        if debug:
            print("troppo dx")

    P = config.RampError
    # D = config.dist_error - config.dist_previous_error
    PIDvalue = (8 * P)
    # config.dist_previous_error = config.dist_error
    # print("PID", PIDvalue)

    if config.RampRightSpeed + PIDvalue > 100:
        config.walk_speed_right = 100
    elif config.RampRightSpeed + PIDvalue < 0:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.RampRightSpeed + PIDvalue

    if config.RampLeftSpeed - PIDvalue > 100:
        config.walk_speed_left = 100
    elif config.RampLeftSpeed - PIDvalue < 0:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.RampLeftSpeed - PIDvalue

    if config.RampCount < 5:
        config.RampCount = config.RampCount + 1
    else:
        config.RampPrevRight = right_dist
        config.RampCount = 0
        # print("10 misure")

