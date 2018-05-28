from RPi import GPIO
import config
import time
import Distance

def Rubble():
    print("Rubble")
    right_dist = Distance.measure_distance(config.US_RIGHT)
    left_dist = Distance.measure_distance(config.US_LEFT)

    print("right",right_dist)
    print("left",left_dist)

    if round(abs(right_dist-left_dist)) < 2:
        config.walk_speed_left = 60
        config.walk_speed_right = 60
    elif right_dist > left_dist:
        config.walk_speed_left = 60
        config.walk_speed_right = 100
    elif left_dist > right_dist:
        config.walk_speed_left = 100
        config.walk_speed_right = 60