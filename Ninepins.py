from RPi import GPIO
import config
import time
import Distance

def Ninepins(debug):
    right_dist = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    left_dist = round(Distance.measure_distance(config.US_LEFT)-1.8,1) #5.8cm ->4cm
    # mid_dist = Distance.measure_distance(config.US_CENTER)
    speed = 50

    if config.dist_count == 10:
        config.previous_dist_left = left_dist

    print("right",right_dist)
    print("left",left_dist)

    if config.previous_dist_left - left_dist > 3.5:
        config.dist_error = 4
        if debug:
            print("troppo sin")
    if config.previous_dist_left - left_dist > 2.5 and config.previous_dist_left - left_dist <= 3.5:
        config.dist_error = 3
        if debug:
            print("quasitroppo sin")
    if config.previous_dist_left - left_dist > 1.5 and config.previous_dist_left - left_dist <= 2.5:
        config.dist_error = 2
        if debug:
            print("unpopiu sin")
    if config.previous_dist_left - left_dist > 0.5 and config.previous_dist_left - left_dist <= 1.5:
        config.dist_error = 1
        if debug:
            print("unpo sin")#gira destra
    if abs(left_dist - config.previous_dist_left) <= 0.5:
        config.dist_error = 0
        if debug:
            print("mid")
    if left_dist - config.previous_dist_left > 0.5 and left_dist - config.previous_dist_left <= 1.5:
        config.dist_error = -1
        if debug:
            print("unpo dx")
    if left_dist - config.previous_dist_left > 1.5 and left_dist - config.previous_dist_left <= 2.5:
        config.dist_error = -2
        if debug:
            print("unpopiu dx")
    if left_dist - config.previous_dist_left > 2.5 and left_dist - config.previous_dist_left  <= 3.5:
        config.dist_error = -3
        if debug:
            print("quasitroppo dx")
    if left_dist - config.previous_dist_left > 3.5:
        config.dist_error = -4
        if debug:
            print("troppo dx")

    P = config.dist_error
    D = config.dist_error - config.dist_previous_error
    PIDvalue = (15 * P)  + (5 * D)
    config.dist_previous_error = config.dist_error
    print("PID", PIDvalue)

    if speed + PIDvalue > 100:
        config.walk_speed_left = 100
    elif speed + PIDvalue < 0:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = speed + PIDvalue

    if speed - PIDvalue > 100:
        config.walk_speed_right = 100
    elif speed - PIDvalue < 0:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = speed - PIDvalue




    if config.dist_count < 5:
        config.dist_count = config.dist_count + 1
    else:
        config.previous_dist_left = left_dist
        config.dist_count = 0
        # print("10 misure")

