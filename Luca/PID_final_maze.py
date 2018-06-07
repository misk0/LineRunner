from RPi import GPIO
import config
import time
import Distance

def follow_distance(debug):
    right_dist = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    left_dist = round(Distance.measure_distance(config.US_LEFT)-1.8,1) #5.8cm ->4cm
    # mid_dist = Distance.measure_distance(config.US_CENTER)

    if config.dist_count == 10:
        config.previous_dist_left = left_dist
        config.previous_dist_right = left_dist #old two

    TotalDist = right_dist + left_dist

    # print("right",right_dist)
    # print("left",left_dist)
    # print("mid",mid_dist)
    if left_dist <= 3.5:
        config.walk_speed_right = 0
        config.walk_speed_left = 100
    elif right_dist <= 3.5:
        config.walk_speed_right = 100
        config.walk_speed_left = 0
    elif left_dist > 35:
        config.drive_left.ChangeDutyCycle(0)
        config.drive_right.ChangeDutyCycle(100)
        time.sleep(0.4)
        config.walk_speed_right = 50
        config.walk_speed_left = 48
    # elif mid_dist < 16.5 and left_dist > right_dist:
    #     config.drive_left.ChangeDutyCycle(0)
    #     config.drive_right.ChangeDutyCycle(100)
    #     time.sleep(1)
    #     config.drive_left.ChangeDutyCycle(65)
    #     config.drive_right.ChangeDutyCycle(82)
    #     time.sleep(0.5)
    #     config.walk_speed_right = 50
    #     config.walk_speed_left = 48
    #     print("hard lelft")
    else:
        # if right_dist > left_dist:
            # if TotalDist > 12.8:
            #     right_dist = 12.8 - left_dist
            #     if right_dist < 0:
            #         right_dist = 0
            #     right_dist = round(right_dist,1)
            #     print("adjusted right",right_dist)
            #     TotalDist = 12.8
            # else:
            #     print("non più destra grande")
            # print("Total", TotalDist)
        #     if TotalDist > 12.8:
        #         left_dist = 12.8 - right_dist
        #         if left_dist < 0:
        #             left_dist = 0
        #         left_dist = round(left_dist,1)
        #         print("adjusted left",left_dist)
        #         TotalDist = 12.8
        #     print("Total", TotalDist)

        # MazeLargeMin = 26
        # RobotLarge = 13.2

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
        D = config.dist_error - config.dist_previous_error
        PIDvalue = (7 * P) + (5 * D)

        print("PID",PIDvalue)

        if config.dist_left_speed + PIDvalue > 100:
            config.walk_speed_left = 100
        elif config.dist_left_speed + PIDvalue < 0:
            config.walk_speed_left = 0
        else:
            config.walk_speed_left = config.dist_left_speed + PIDvalue

        if config.dist_right_speed - PIDvalue > 100:
            config.walk_speed_right = 100
        elif config.dist_right_speed - PIDvalue < 0:
            config.walk_speed_right = 0
        else:
            config.walk_speed_right = config.dist_right_speed - PIDvalue

        print("speed left",config.walk_speed_left)
        print("speed right", config.walk_speed_right)
        print("prev left",config.previous_dist_left)

        if config.dist_count < 1:
            config.dist_count = config.dist_count + 1
        else:
            config.previous_dist_right = left_dist
            config.dist_count = 0

        config.previous_dist_left = left_dist


    config.dist_previous_error = config.dist_error