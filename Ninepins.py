from RPi import GPIO
import config
import time
import Distance

def Ninepins(debug):
    right_dist = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    left_dist = round(Distance.measure_distance(config.US_LEFT)-1.8,1) #5.8cm ->4cm

    if config.NinepinsCount == 10:
        config.NinepinsPrevLeft = left_dist

    # print("right",right_dist)
    # print("left",left_dist)

    if config.NinepinsPrevLeft - left_dist > 3.5:
        config.NinepinsError = 4
        if debug:
            print("troppo sin")
    if config.NinepinsPrevLeft - left_dist > 2.5 and config.NinepinsPrevLeft - left_dist <= 3.5:
        config.NinepinsError = 3
        if debug:
            print("quasitroppo sin")
    if config.NinepinsPrevLeft - left_dist > 1.5 and config.NinepinsPrevLeft - left_dist <= 2.5:
        config.NinepinsError = 2
        if debug:
            print("unpopiu sin")
    if config.NinepinsPrevLeft - left_dist > 0.5 and config.NinepinsPrevLeft - left_dist <= 1.5:
        config.NinepinsError = 1
        if debug:
            print("unpo sin")#gira destra
    if abs(left_dist - config.NinepinsPrevLeft) <= 0.5:
        config.NinepinsError = 0
        if debug:
            print("mid")
    if left_dist - config.NinepinsPrevLeft > 0.5 and left_dist - config.NinepinsPrevLeft <= 1.5:
        config.NinepinsError = -1
        if debug:
            print("unpo dx")
    if left_dist - config.NinepinsPrevLeft > 1.5 and left_dist - config.NinepinsPrevLeft <= 2.5:
        config.NinepinsError = -2
        if debug:
            print("unpopiu dx")
    if left_dist - config.NinepinsPrevLeft > 2.5 and left_dist - config.NinepinsPrevLeft  <= 3.5:
        config.NinepinsError = -3
        if debug:
            print("quasitroppo dx")
    if left_dist - config.NinepinsPrevLeft > 3.5:
        config.NinepinsError = -4
        if debug:
            print("troppo dx")

    P = config.NinepinsError
    D = config.NinepinsError - config.NinepinsPrevError
    PIDvalue = (15 * P)  + (5 * D)
    config.NinepinsPrevError = config.NinepinsError
    # print("PID", PIDvalue)

    if config.NinepinsLeftSpeed + PIDvalue > 100:
        config.walk_speed_left = 100
    elif config.NinepinsLeftSpeed + PIDvalue < 0:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.NinepinsLeftSpeed + PIDvalue

    if config.NinepinsRightSpeed - PIDvalue > 100:
        config.walk_speed_right = 100
    elif config.NinepinsRightSpeed - PIDvalue < 0:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.NinepinsRightSpeed - PIDvalue

    if config.NinepinsCount < 5:
        config.NinepinsCount = config.NinepinsCount + 1
    else:
        config.NinepinsPrevLeft = left_dist
        config.NinepinsCount = 0
        # print("10 misure")

