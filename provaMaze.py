from RPi import GPIO
import config
import time
import Distance

def follow_distance(debug):
    right_dist = round(Distance.measure_distance(config.US_RIGHT)-1.8,1) #6.1cm ->4.3cm
    left_dist = round(Distance.measure_distance(config.US_LEFT)-1.8,1) #5.8cm ->4cm
    # mid_dist = Distance.measure_distance(config.US_CENTER)

    print("right",right_dist)
    print("left",left_dist)

    if left_dist <= 3.5:
        config.walk_speed_right = 20
        config.walk_speed_left = 100
    elif left_dist > 3.5 and left_dist <= 3.8:
    # go semi hard right
        config.drive_left.ChangeDutyCycle(100)
        config.drive_right.ChangeDutyCycle(40)
    elif left_dist > 3.8 and left_dist <= 4.1:
    # go semi soft right
        config.drive_left.ChangeDutyCycle(100)
        config.drive_right.ChangeDutyCycle(60)
    elif left_dist > 4.1 and left_dist <= 4.3:
    #go soft right
        config.drive_left.ChangeDutyCycle(75)
        config.drive_right.ChangeDutyCycle(75)
    elif left_dist > 4.3 and left_dist <= 4.7:
        #go FW
        config.drive_left.ChangeDutyCycle(55)
        config.drive_right.ChangeDutyCycle(72)
    elif left_dist > 4.7 and left_dist <= 4.9:
    #go soft left
        config.drive_left.ChangeDutyCycle(55)
        config.drive_right.ChangeDutyCycle(90)
    elif left_dist > 4.9 and left_dist <= 5.2:
    # go semi soft left
        config.drive_left.ChangeDutyCycle(50)
        config.drive_right.ChangeDutyCycle(100)
    elif left_dist > 5.2 and left_dist <= 5.5:
    # go semi hard right
        config.drive_left.ChangeDutyCycle(35)
        config.drive_right.ChangeDutyCycle(100)
    elif left_dist > 5.5:
        config.walk_speed_right = 100
        config.walk_speed_left = 20