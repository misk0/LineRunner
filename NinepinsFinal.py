from RPi import GPIO
import config
import time
import Distance

def follow_distance(debug):
    right_dist = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    left_dist = round(Distance.measure_distance(config.US_LEFT)-1.8,1) #5.8cm ->4cm

    TotalDist = right_dist + left_dist

    # print("right",right_dist)
    # print("left",left_dist)

    if left_dist <= 3.5:
        config.walk_speed_right = 0
        config.walk_speed_left = 100
    elif right_dist <= 3.5:
        config.walk_speed_right = 100
        config.walk_speed_left = 0
    else:
        if left_dist <= (1/9)*TotalDist:
            config.NinepinsFinalError = 4
            if debug:
                print("troppo sin")
        if left_dist <= (2/9)*TotalDist and left_dist > (1/9)*TotalDist:
            config.NinepinsFinalError = 3
            if debug:
                print("quasitroppo sin")
        if left_dist <= (3/9)*TotalDist and left_dist > (2/9)*TotalDist:
            config.NinepinsFinalError = 2
            if debug:
                print("unpopiu sin")
        if left_dist <= (4/9)*TotalDist and left_dist > (3/9)*TotalDist:
            config.NinepinsFinalError = 1
            if debug:
                print("unpo sin")
        if left_dist > (4/9)*TotalDist and right_dist > (4/9)*TotalDist:
            config.NinepinsFinalError = 0
            if debug:
                print("mid")
        if right_dist <= (4/9)*TotalDist and right_dist > (3/9)*TotalDist:
            config.NinepinsFinalError = -1
            if debug:
                print("unpo dx")
        if right_dist <= (3/9)*TotalDist and right_dist > (2/9)*TotalDist:
            config.NinepinsFinalError = -2
            if debug:
                print("unpopiu dx")
        if right_dist <= (2/9)*TotalDist and right_dist > (1/9)*TotalDist:
            config.NinepinsFinalError = -3
            if debug:
                print("quasitroppo dx")
        if right_dist <= (1/9)*TotalDist:
            config.NinepinsFinalError = -4
            if debug:
                print("troppo dx")

        P = config.NinepinsFinalError
        D = config.NinepinsFinalError - config.NinepinsFinalPrevError
        PIDvalue = (7 * P) + (5 * D)
        config.NinepinsFinalPrevError = config.NinepinsFinalError

        # print("PID",PIDvalue)

        if config.NinepinsFinalLeftSpeed + PIDvalue > 100:
            config.walk_speed_left = 100
        elif config.NinepinsFinalLeftSpeed + PIDvalue < 0:
            config.walk_speed_left = 0
        else:
            config.walk_speed_left = config.NinepinsFinalLeftSpeed + PIDvalue

        if config.NinepinsFinalRightSpeed - PIDvalue > 100:
            config.walk_speed_right = 100
        elif config.NinepinsFinalRightSpeed - PIDvalue < 0:
            config.walk_speed_right = 0
        else:
            config.walk_speed_right = config.NinepinsFinalRightSpeed - PIDvalue

        # print("speed left",config.walk_speed_left)
        # print("speed right", config.walk_speed_right)



