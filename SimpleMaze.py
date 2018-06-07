from RPi import GPIO
import config
import time
import Distance

def follow_distance(debug):
    right_dist = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    left_dist = round(Distance.measure_distance(config.US_LEFT)-1.8,1) #5.8cm ->4cm
    # mid_dist = Distance.measure_distance(config.US_CENTER)

    if config.SimpleMazeCount == 10:
        config.PreviousDistLeft_SimpleMaze = left_dist

    # print("right",right_dist)
    # print("left",left_dist)

    if left_dist > 20:
        config.drive_left.ChangeDutyCycle(0)
        config.drive_right.ChangeDutyCycle(100)
        time.sleep(0.4)
        config.walk_speed_right = 50
        config.walk_speed_left = 48
        config.SimpleMazeCount = 10
        config.SimpleMazeSpeed = 35
        config.EndSimpleMaze = True
        config.SimpleMazeLeftDone = True
    elif config.SimpleMazeLeftDone == True and right_dist > 25:
        config.drive_left.ChangeDutyCycle(100)
        config.drive_right.ChangeDutyCycle(0)
        time.sleep(0.5)
        config.walk_speed_right = 45
        config.walk_speed_left = 45
        config.SimpleMazeCount = 10
    else:
        if config.PreviousDistLeft_SimpleMaze - left_dist > 3.5:
            config.SimpleMazeError = 4
            if debug:
                print("troppo sin")
        if config.PreviousDistLeft_SimpleMaze - left_dist > 2.5 and config.PreviousDistLeft_SimpleMaze - left_dist <= 3.5:
            config.SimpleMazeError = 3
            if debug:
                print("quasitroppo sin")
        if config.PreviousDistLeft_SimpleMaze - left_dist > 1.5 and config.PreviousDistLeft_SimpleMaze - left_dist <= 2.5:
            config.SimpleMazeError = 2
            if debug:
                print("unpopiu sin")
        if config.PreviousDistLeft_SimpleMaze - left_dist > 0.5 and config.PreviousDistLeft_SimpleMaze - left_dist <= 1.5:
            config.SimpleMazeError = 1
            if debug:
                print("unpo sin")#gira destra
        if abs(left_dist - config.PreviousDistLeft_SimpleMaze) <= 0.5:
            config.SimpleMazeError = 0
            if debug:
                print("mid")
        if left_dist - config.PreviousDistLeft_SimpleMaze > 0.5 and left_dist - config.PreviousDistLeft_SimpleMaze <= 1.5:
            config.SimpleMazeError = -1
            if debug:
                print("unpo dx")
        if left_dist - config.PreviousDistLeft_SimpleMaze > 1.5 and left_dist - config.PreviousDistLeft_SimpleMaze <= 2.5:
            config.SimpleMazeError = -2
            if debug:
                print("unpopiu dx")
        if left_dist - config.PreviousDistLeft_SimpleMaze > 2.5 and left_dist - config.PreviousDistLeft_SimpleMaze <= 3.5:
            config.SimpleMazeError = -3
            if debug:
                print("quasitroppo dx")
        if left_dist - config.PreviousDistLeft_SimpleMaze > 3.5:
            config.SimpleMazeError = -4
            if debug:
                print("troppo dx")

        P = config.SimpleMazeError
        D = config.SimpleMazeError - config.SimpleMazePrevError
        PIDvalue = (15 * P)  + (2 * D)
        config.SimpleMazePrevError = config.SimpleMazeError
        # print("PID", PIDvalue)

        if config.SimpleMazeSpeed + PIDvalue > 100:
            config.walk_speed_left = 100
        elif config.SimpleMazeSpeed + PIDvalue < 0:
            config.walk_speed_left = 0
        else:
            config.walk_speed_left = config.SimpleMazeSpeed + PIDvalue

        if config.SimpleMazeSpeed - PIDvalue > 100:
            config.walk_speed_right = 100
        elif config.SimpleMazeSpeed - PIDvalue < 0:
            config.walk_speed_right = 0
        else:
            config.walk_speed_right = config.SimpleMazeSpeed - PIDvalue




        if config.SimpleMazeCount < 4:
            config.SimpleMazeCount = config.SimpleMazeCount + 1
        else:
            config.PreviousDistLeft_SimpleMaze = left_dist
            config.SimpleMazeCount = 0
            # print("10 misure")