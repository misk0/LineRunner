from RPi import GPIO
import config
import time
import Distance

def follow_distance(debug):
    right_dist = Distance.measure_distance(config.US_RIGHT)
    left_dist = Distance.measure_distance(config.US_LEFT)

    print("right",right_dist)
    print("left",left_dist)

    TotalDist = right_dist+left_dist
    # MazeLargeMin = 26
    # RobotLarge = 13.2
    # Mid = (MazeLargeMin - RobotLarge)/2 #6.4
    # troppoSin = 4
    # troppoDes = troppoSin
    # Step = (Mid - troppoSin)/4 #0.6
    # QuasiTroppoSin = Step + (Step/3) + troppoSin #4.8
    # QuasiTroppoDes = QuasiTroppoSin
    # UnPoPiuSin = (Step + (Step/3))*2 + troppoSin #5.6
    # UnPoPiuDes = UnPoPiuSin

    # if right_dist > left_dist and right_dist > Mid:
    #     config.dist_error = 5
    #     print("estremo dx")
    #
    # if left_dist > right_dist and left_dist > Mid:
    #     config.dist_error = -5
    #     print("estremo sx")
    #
    # if left_dist < troppoSin:
    #     config.dist_error = 4
    #     if debug:
    #         print("troppo sin")
    # if left_dist >= troppoSin and left_dist < QuasiTroppoSin:
    #     config.dist_error = 3
    #     if debug:
    #         print("quasitroppo sin")
    #
    # if left_dist >= QuasiTroppoSin and left_dist < UnPoPiuSin:
    #     config.dist_error = 2
    #     if debug:
    #         print("unpopiu sin")
    # if left_dist >= UnPoPiuSin and left_dist < Mid:
    #     config.dist_error = 1
    #     if debug:
    #         print("unpo sin")
    # if left_dist >= Mid and right_dist >= Mid and abs(left_dist - right_dist) < 3:
    #     config.dist_error = 0
    #     if debug:
    #         print("mid")
    # if right_dist >= UnPoPiuDes and right_dist < Mid:
    #     config.dist_error = -1
    #     if debug:
    #         print("unpo dx")
    # if right_dist >= QuasiTroppoDes and right_dist < UnPoPiuDes:
    #     config.dist_error = -2
    #     if debug:
    #         print("unpopiu dx")
    # if right_dist >= troppoDes and right_dist < QuasiTroppoDes:
    #     config.dist_error = -3
    #     if debug:
    #         print("quasitroppo dx")
    # if right_dist < troppoDes:
    #     config.dist_error = -4
    #     if debug:
    #         print("troppo dx")

    if left_dist <= (1/9)*TotalDist:
        config.dist_error = 4
        if debug:
            print("troppo sin")
    if left_dist <= (2/9)*TotalDist and left_dist > (1/9)*TotalDist:
        config.dist_error = 3
        if debug:
            print("quasitroppo sin")

    if left_dist <= (3/9)*TotalDist and left_dist > (2/9)*TotalDist:
        config.dist_error = 2
        if debug:
            print("unpopiu sin")
    if left_dist <= (4/9)*TotalDist and left_dist > (3/9)*TotalDist:
        config.dist_error = 1
        if debug:
            print("unpo sin")
    if left_dist > (4/9)*TotalDist and right_dist > (4/9)*TotalDist:
        config.dist_error = 0
        if debug:
            print("mid")
    if right_dist <= (4/9)*TotalDist and right_dist > (3/9)*TotalDist:
        config.dist_error = -1
        if debug:
            print("unpo dx")
    if right_dist <= (3/9)*TotalDist and right_dist > (2/9)*TotalDist:
        config.dist_error = -2
        if debug:
            print("unpopiu dx")
    if right_dist <= (2/9)*TotalDist and right_dist > (1/9)*TotalDist:
        config.dist_error = -3
        if debug:
            print("quasitroppo dx")
    if right_dist <= (1/9)*TotalDist:
        config.dist_error = -4
        if debug:
            print("troppo dx")



    P = config.dist_error
    #D = config.dist_error - config.dist_previous_error
    PIDvalue = (config.dist_kp * P) #+ (config.dist_kd * D)

    print("PID",PIDvalue)

    if config.dist_left_speed + PIDvalue > 100:
        config.walk_speed_left = 100
    elif config.dist_left_speed + PIDvalue < config.min_left_speed:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.dist_left_speed + PIDvalue

    if config.dist_right_speed - PIDvalue > 100:
        config.walk_speed_right = 100
    elif config.dist_right_speed - PIDvalue < config.min_right_speed:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.dist_right_speed - PIDvalue

    print("speed left",config.walk_speed_left)
    print("speed right", config.walk_speed_right)

    # config.dist_previous_error = config.dist_error