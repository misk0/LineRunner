import RPi.GPIO as GPIO
import time
import config


def measure_distance(sensor_pos, debug=False):
    complex_distance = 0
    retries = 0
    pulse_start = 0
    pulse_end = 0
    for counter in range(5):
        GPIO.output(config.ultrasonic_triggers[sensor_pos], GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(config.ultrasonic_triggers[sensor_pos], GPIO.LOW)
        while GPIO.input(config.ultrasonic_echo[sensor_pos]) == 0:
            pulse_start = time.time()

        while GPIO.input(config.ultrasonic_echo[sensor_pos]) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance,1)
        if debug:
            print("Sensor : %s Current distance: %s" % (sensor_pos, distance))
        if complex_distance == 0:
            complex_distance = distance

        if distance < complex_distance:
            complex_distance = distance
        time.sleep(0.05)

    return complex_distance

def follow_distance(debug=True):
    distance_left = measure_distance(config.US_LEFT, False)
    distance_middle = measure_distance(config.US_CENTER, False)
    distance_right = measure_distance(config.US_RIGHT, False)

    if debug:
        print("Left distance: ", distance_left)
        print("Middle distance: ", distance_middle)
        print("Right distance: ", distance_right)

    if distance_right <= config.Distance_MinValue:
        config.dist_error = -4
        if debug:
            print("DistRight too small, go left")
    elif distance_left <= config.Distance_MinValue:
        config.dist_error = 4
        if debug:
            print("DistLeft too small, go right")
    elif distance_right > distance_middle and distance_right > distance_left:
        config.dist_error = 3
        if debug:
            print("DistRight big, go right")
    elif distance_middle > distance_right and distance_middle > distance_left:
        config.dist_error = 0
        if debug:
            print("Distmid big, go FW")
    elif distance_left > distance_middle and distance_left > distance_right:
        config.dist_error = -3
        if debug:
            print("DistLeft big, go left")

    P = config.dist_error
    config.dist_integrative = config.dist_integrative + config.dist_error
    D = config.dist_error - config.dist_previous_error
    PIDvalue = (config.dist_kp * P) + (config.dist_ki * config.dist_integrative) + (config.dist_kd * D)

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



