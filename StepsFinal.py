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
            config.StepsFinalError = 4
            if debug:
                print("troppo sin")
        if left_dist <= (2/9)*TotalDist and left_dist > (1/9)*TotalDist:
            config.StepsFinalError = 3
            if debug:
                print("quasitroppo sin")
        if left_dist <= (3/9)*TotalDist and left_dist > (2/9)*TotalDist:
            config.StepsFinalError = 2
            if debug:
                print("unpopiu sin")
        if left_dist <= (4/9)*TotalDist and left_dist > (3/9)*TotalDist:
            config.StepsFinalError = 1
            if debug:
                print("unpo sin")
        if left_dist > (4/9)*TotalDist and right_dist > (4/9)*TotalDist:
            config.StepsFinalError = 0
            if debug:
                print("mid")
        if right_dist <= (4/9)*TotalDist and right_dist > (3/9)*TotalDist:
            config.StepsFinalError = -1
            if debug:
                print("unpo dx")
        if right_dist <= (3/9)*TotalDist and right_dist > (2/9)*TotalDist:
            config.StepsFinalError = -2
            if debug:
                print("unpopiu dx")
        if right_dist <= (2/9)*TotalDist and right_dist > (1/9)*TotalDist:
            config.StepsFinalError = -3
            if debug:
                print("quasitroppo dx")
        if right_dist <= (1/9)*TotalDist:
            config.StepsFinalError = -4
            if debug:
                print("troppo dx")

        P = config.StepsFinalError
        D = config.StepsFinalError - config.StepsFinalPrevError
        PIDvalue = (7 * P) + (5 * D)
        config.StepsFinalPrevError = config.StepsFinalError

        # print("PID",PIDvalue)

        if config.StepsFinalLeftSpeed + PIDvalue > 100:
            config.walk_speed_left = 100
        elif config.StepsFinalLeftSpeed + PIDvalue < 0:
            config.walk_speed_left = 0
        else:
            config.walk_speed_left = config.StepsFinalLeftSpeed + PIDvalue

        if config.StepsFinalRightSpeed - PIDvalue > 100:
            config.walk_speed_right = 100
        elif config.StepsFinalRightSpeed - PIDvalue < 0:
            config.walk_speed_right = 0
        else:
            config.walk_speed_right = config.StepsFinalRightSpeed - PIDvalue

        # print("speed left",config.walk_speed_left)
        # print("speed right", config.walk_speed_right)