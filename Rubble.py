from RPi import GPIO
import config
import time
import Distance

def Rubble():
    print("Rubble")
    left_dist = Distance.measure_distance(config.US_RIGHT)
    right_dist = Distance.measure_distance(config.US_LEFT)

    print("right",right_dist)
    print("left",left_dist)

    if abs(left_dist - config.pervious_dist_left) < 2 or  abs(right_dist - config.pervious_dist_right) < 2:
        print("mid")
        config.walk_speed_left = 80
        config.walk_speed_right = 80
    elif right_dist > left_dist:
        print("turn left")
        config.walk_speed_left = 20
        config.walk_speed_right = 80
    elif left_dist > right_dist:
        print("turn right")
        config.walk_speed_left = 80
        config.walk_speed_right = 20

    config.pervious_dist_left = left_dist
    config.pervious_dist_right = right_dist