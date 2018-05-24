from RPi import GPIO
import config
import time
import Distance

def follow_distance(debug=False):
    right_dist = Distance.measure_distance(config.US_RIGHT)
    left_dist = Distance.measure_distance(config.US_LEFT)

    MazeLargeMin = 30
    RobotLarge = 12
    Mid = (MazeLargeMin - RobotLarge)/2
    troppoSin = 5
    troppoDes = troppoSin
    Step = (Mid - troppoSin)/4
    QuasiTroppoSin = Step + (Step/3) + troppoSin
    QuasiTroppoDes = QuasiTroppoSin
    UnPoPiuSin = (Step + (Step/3))*2 + troppoSin
    UnPoPiuDes = UnPoPiuSin


    if left_dist < troppoSin:
        config.dist_error = 4
        if debug:
            print("troppo sin")
    if left_dist >= troppoSin and left_dist < QuasiTroppoSin:
        config.dist_error = 3
        if debug:
            print("quasitroppo sin")

    if left_dist >= QuasiTroppoSin and left_dist < UnPoPiuSin:
        config.dist_error = 2
        if debug:
            print("unpopiu sin")
    if left_dist >= UnPoPiuSin and left_dist < Mid:
        config.dist_error = 1
        if debug:
            print("unpo sin")
    if left_dist == Mid or right_dist == Mid:
        config.dist_error = 0
        if debug:
            print("mid")
    if right_dist >= UnPoPiuDes and right_dist < Mid:
        config.dist_error = -1
        if debug:
            print("unpo dx")
    if right_dist >= QuasiTroppoDes and right_dist < UnPoPiuDes:
        config.dist_error = -2
        if debug:
            print("unpopiu dx")
    if right_dist >= troppoDes and right_dist < QuasiTroppoDes:
        config.dist_error = -3
        if debug:
            print("quasitroppo sx")
    if right_dist < troppoDes:
        config.dist_error = -4
        if debug:
            print("troppo dx")

    P = config.dist_error
    D = config.dist_error - config.dist_previous_error
    PIDvalue = (config.dist_kp * P) + (config.dist_kd * D)

    if config.dist_left_speed - PIDvalue > 100:
        config.walk_speed_left = 100
    elif config.dist_left_speed - PIDvalue < config.min_left_speed:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.dist_left_speed - PIDvalue

    if config.dist_right_speed + PIDvalue > 100:
        config.walk_speed_right = 100
    elif config.dist_right_speed + PIDvalue < config.min_right_speed:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.dist_right_speed + PIDvalue

    config.dist_previous_error = config.dist_error