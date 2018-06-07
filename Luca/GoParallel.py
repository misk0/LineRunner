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

    print("right",right_dist)
    print("left",left_dist)
    if GPIO.input(config.line_follow_lmax) and GPIO.input(config.line_follow_lmin) and GPIO.input(config.line_follow_mid) and GPIO.input(config.line_follow_rmin) and GPIO.input(config.line_follow_rmax):
        config.walk_speed_right = 100
        config.walk_speed_left = 100
    else:
        # if mid_dist > 6:
        if right_dist <= 5:
            config.walk_speed_right = 100
            config.walk_speed_left = 0
            print("hard left")
        elif left_dist <= 6:
            config.walk_speed_right = 0
            config.walk_speed_left = 100
            print("hard right")
        elif left_dist - right_dist > 20:
            config.walk_speed_right = 100
            config.walk_speed_left = 0
            print("hard left")
        elif right_dist - left_dist > 20:
            config.walk_speed_right = 0
            config.walk_speed_left = 100
            print("hard right")
        elif abs(left_dist-config.previous_dist_left) <= 0.5:
            config.walk_speed_right = 82
            config.walk_speed_left = 65
            print("FW")
        elif config.previous_dist_left > left_dist:
            config.walk_speed_right = 60
            config.walk_speed_left = 100
            print("soft right")
        else:
            config.walk_speed_right = 100
            config.walk_speed_left = 35
            print("soft left")


        if config.dist_count < 5:
            config.dist_count = config.dist_count + 1
        else:
            config.previous_dist_left = left_dist
            config.dist_count = 0
            # print("10 misure")

    # else:
    #     config.walk_speed_right = 35
    #     config.walk_speed_left = 80



    # TotalDist = right_dist+left_dist
    # # RobotLarge = 13.2
    #
