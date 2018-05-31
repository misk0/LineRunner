from RPi import GPIO
import config
import time
import Distance

def follow_distance(debug):
    right_dist = Distance.measure_distance(config.US_RIGHT)
    left_dist = Distance.measure_distance(config.US_LEFT)
    mid_dist = Distance.measure_distance(config.US_CENTER)

    print("right",right_dist)
    print("left",left_dist)

    if mid_dist > left_dist and mid_dist > right_dist and right_dist > 4 and left_dist > 4:
        config.walk_speed_right = 80
        config.walk_speed_left = 60
    elif left_dist <= 4:
        config.walk_speed_right = 0
        config.walk_speed_left = 100
    elif right_dist <= 4:
        config.walk_speed_right = 100
        config.walk_speed_left = 0
    elif right_dist > left_dist:
        config.walk_speed_right = 40
        config.walk_speed_left = 80
    elif left_dist > right_dist:
        config.walk_speed_right = 80
        config.walk_speed_left = 40