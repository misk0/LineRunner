from RPi import GPIO
import config
import time
import Distance

def follow_distance(debug):
    right_dist = Distance.measure_distance(config.US_RIGHT)
    left_dist = Distance.measure_distance(config.US_LEFT)
    # mid_dist = Distance.measure_distance(config.US_CENTER)

    if config.dist_count == 10:
        config.previous_dist_left = left_dist

    # print("right",right_dist)
    # print("left",left_dist)
    if GPIO.input(config.line_follow_lmax) and GPIO.input(config.line_follow_lmin) and GPIO.input(config.line_follow_mid) and GPIO.input(config.line_follow_rmin) and GPIO.input(config.line_follow_rmax):
        config.walk_speed_right = 100
        config.walk_speed_left = 100
    else:
        # if mid_dist > 6:
        if right_dist <= 4:
            config.walk_speed_right = 80
            config.walk_speed_left = 35
        elif left_dist <= 4:
            config.walk_speed_right = 35
            config.walk_speed_left = 80
        elif abs(left_dist-config.previous_dist_left) <= 1:
            config.walk_speed_right = 80
            config.walk_speed_left = 80
        elif config.previous_dist_left > left_dist:
            config.walk_speed_right = 60
            config.walk_speed_left = 80
        else:
            config.walk_speed_right = 80
            config.walk_speed_left = 60

        if config.dist_count < 9:
            config.dist_count = config.dist_count + 1
        else:
            config.previous_dist_left = left_dist
            config.dist_count = 0
            print("10 misure")

    # else:
    #     config.walk_speed_right = 35
    #     config.walk_speed_left = 80



    # TotalDist = right_dist+left_dist
    # # RobotLarge = 13.2
    #
    # if left_dist <= (1/9)*TotalDist:
    #     config.dist_error = 4
    #     if debug:
    #         print("troppo sin")
    # if left_dist <= (2/9)*TotalDist and left_dist > (1/9)*TotalDist:
    #     config.dist_error = 3
    #     if debug:
    #         print("quasitroppo sin")
    #
    # if left_dist <= (3/9)*TotalDist and left_dist > (2/9)*TotalDist:
    #     config.dist_error = 2
    #     if debug:
    #         print("unpopiu sin")
    # if left_dist <= (4/9)*TotalDist and left_dist > (3/9)*TotalDist:
    #     config.dist_error = 1
    #     if debug:
    #         print("unpo sin")
    # if left_dist > (4/9)*TotalDist and right_dist > (4/9)*TotalDist:
    #     config.dist_error = 0
    #     if debug:
    #         print("mid")
    # if right_dist <= (4/9)*TotalDist and right_dist > (3/9)*TotalDist:
    #     config.dist_error = -1
    #     if debug:
    #         print("unpo dx")
    # if right_dist <= (3/9)*TotalDist and right_dist > (2/9)*TotalDist:
    #     config.dist_error = -2
    #     if debug:
    #         print("unpopiu dx")
    # if right_dist <= (2/9)*TotalDist and right_dist > (1/9)*TotalDist:
    #     config.dist_error = -3
    #     if debug:
    #         print("quasitroppo dx")
    # if right_dist <= (1/9)*TotalDist:
    #     config.dist_error = -4
    #     if debug:
    #         print("troppo dx")
    #
    #
    #
    # P = config.dist_error
    # #D = config.dist_error - config.dist_previous_error
    # PIDvalue = (config.dist_kp * P) #+ (config.dist_kd * D)
    #
    # print("PID",PIDvalue)
    #
    # if config.dist_left_speed + PIDvalue > 100:
    #     config.walk_speed_left = 100
    # elif config.dist_left_speed + PIDvalue < config.min_left_speed:
    #     config.walk_speed_left = 0
    # else:
    #     config.walk_speed_left = config.dist_left_speed + PIDvalue
    #
    # if config.dist_right_speed - PIDvalue > 100:
    #     config.walk_speed_right = 100
    # elif config.dist_right_speed - PIDvalue < config.min_right_speed:
    #     config.walk_speed_right = 0
    # else:
    #     config.walk_speed_right = config.dist_right_speed - PIDvalue
    #
    # print("speed left",config.walk_speed_left)
    # print("speed right", config.walk_speed_right)