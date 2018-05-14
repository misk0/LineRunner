import config
from RPi import GPIO
from threading import Thread
import time
import RFIDReader
import FoundInSpace
import signal
import sys
import Distance

config.init()

#GPIO.setmode(GPIO.BOARD)

# Create thread for RFID reading
rfid = RFIDReader.RFIDReader()
rfidThread = Thread(target=rfid.run)
rfidThread.start()

#distance = FoundInSpace.FoundInSpace()
#distanceThread = Thread(target=distance.run)
#distanceThread.start()

# Initialise objects for H-Bridge GPIO PWM pins
GPIO.setup(config.left_motor_pwm, GPIO.OUT)
GPIO.setup(config.left_motor_direction, GPIO.OUT)
GPIO.setup(config.left_motor_direction_inv, GPIO.OUT)
GPIO.setup(config.right_motor_pwm, GPIO.OUT)
GPIO.setup(config.right_motor_direction, GPIO.OUT)
GPIO.setup(config.right_motor_direction_inv, GPIO.OUT)

config.drive_left = GPIO.PWM(config.left_motor_pwm, 100)
config.drive_right = GPIO.PWM(config.right_motor_pwm, 100)

# Helper functions
# Initialise objects for H-Bridge digital GPIO pins
back = False

if back:
    GPIO.output(config.left_motor_direction, GPIO.LOW)
    GPIO.output(config.left_motor_direction_inv, GPIO.HIGH)
    GPIO.output(config.right_motor_direction, GPIO.LOW)
    GPIO.output(config.right_motor_direction_inv, GPIO.HIGH)

if not back:
    GPIO.output(config.left_motor_direction, GPIO.HIGH)
    GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
    GPIO.output(config.right_motor_direction, GPIO.HIGH)
    GPIO.output(config.right_motor_direction_inv, GPIO.LOW)


# Initialize distance sensors
GPIO.setup(config.ultrasonic_triggers[config.US_LEFT], GPIO.OUT)
GPIO.setup(config.ultrasonic_triggers[config.US_CENTER], GPIO.OUT)
GPIO.setup(config.ultrasonic_triggers[config.US_RIGHT], GPIO.OUT)
GPIO.setup(config.ultrasonic_pins[config.US_LEFT], GPIO.OUT)
GPIO.setup(config.ultrasonic_pins[config.US_CENTER], GPIO.OUT)
GPIO.setup(config.ultrasonic_pins[config.US_RIGHT], GPIO.OUT)

# Initialize line sensors
GPIO.setup(config.line_follow_sxmax, GPIO.IN)
GPIO.setup(config.line_follow_sxmin, GPIO.IN)
GPIO.setup(config.line_follow_mid, GPIO.IN)
GPIO.setup(config.line_follow_dxmin, GPIO.IN)
GPIO.setup(config.line_follow_dxmax, GPIO.IN)

def end_read(signal,frame):
    print("\nCtrl+C captured, ending read.")
    config.drive_left.stop()
    config.drive_right.stop()
    rfid.terminate()
    GPIO.cleanup()
    sys.exit()

def measure_distance(sensor_id, debug=False):
    complex_distance = 0
    retries = 0
    pulse_start = 0
    pulse_end = 0

    for counter in range(3):
        GPIO.output(config.ultrasonic_trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(config.ultrasonic_trigger_pin, GPIO.LOW)
        while GPIO.input(sensor_id) == 0:
            pulse_start = time.time()

        while GPIO.input(sensor_id) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if debug:
            print("Sensor: %s Current distance: %s" % (sensor_id, distance))
        if 0 < distance < 400:
            retries += 1
            complex_distance += distance
        time.sleep(0.05)

    if retries > 0:
        complex_distance = round(complex_distance / retries, 2)
    return complex_distance

def follow_distance(debug=False):
    DistanceLeft = Distance.measure_distance(config.US_LEFT, False)
    DistanceMid = Distance.measure_distance(config.US_CENTER, False)
    DistanceRight = Distance.measure_distance(config.US_RIGHT, False)

    if DistanceRight <= config.Distance_MinValue:
        config.line_error = -4
        if debug:
            print("DistRight too small, go left")
    elif DistanceLeft <= config.Distance_MinValue:
        config.line_error = 4
        if debug:
            print("DistLeft too small, go right")
    elif DistanceRight > DistanceMid and DistanceRight > DistanceLeft:
        config.line_error = 3
        if debug:
            print("DistRight big, go right")
    elif DistanceMid > DistanceRight and DistanceMid > DistanceLeft:
        config.line_error = 0
        if debug:
            print("Distmid big, go FW")
    elif DistanceLeft > DistanceMid and DistanceLeft > DistanceRight:
        config.line_error = -3
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

def follow_line(debug=False):
    lineSxMaxValue = GPIO.input(config.line_follow_sxmax)
    lineSxMinValue = GPIO.input(config.line_follow_sxmin)
    lineMidValue = GPIO.input(config.line_follow_mid)
    lineDxMinValue = GPIO.input(config.line_follow_dxmin)
    lineDxMaxValue = GPIO.input(config.line_follow_dxmax)
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 0 and lineDxMinValue == 0 and lineDxMaxValue == 1:
        config.line_error = 4
        if debug:
            print("troppo sin")
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 0 and lineDxMinValue == 1 and lineDxMaxValue == 1:
        config.line_error = 3
        if debug:
            print("quasitroppo sin")
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 0 and lineDxMinValue == 1 and lineDxMaxValue == 0:
        config.line_error = 2
        if debug:
            print("unpopiu sin")
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 1 and lineDxMinValue == 1 and lineDxMaxValue == 0:
        config.line_error = 1
        if debug:
            print("unpo sin")
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 1 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        config.line_error = 0
        if debug:
            print("mid")
    if lineSxMaxValue == 0 and lineSxMinValue == 1 and lineMidValue == 1 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        config.line_error = -1
        if debug:
            print("unpo dx")
    if lineSxMaxValue == 0 and lineSxMinValue == 1 and lineMidValue == 0 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        config.line_error = -2
        if debug:
            print("unpopiu dx")
    if lineSxMaxValue == 1 and lineSxMinValue == 1 and lineMidValue == 0 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        config.line_error = -3
        if debug:
            print("quasitroppo sx")
    if lineSxMaxValue == 1 and lineSxMinValue == 0 and lineMidValue == 0 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        config.line_error = -4
        if debug:
            print("troppo dx")

    P = config.line_error
    config.line_integrative = config.line_integrative + config.line_error
    D = config.line_error - config.previous_error
    PIDvalue = (config.line_kp * P) + (config.line_ki * config.line_integrative) + (config.line_kd * D)

    if config.line_left_speed - PIDvalue > 100:
        config.walk_speed_left = 100
    elif config.line_left_speed - PIDvalue < config.min_left_speed:
        config.walk_speed_left = 0
    else:
        config.walk_speed_left = config.line_left_speed - PIDvalue

    if config.line_right_speed + PIDvalue > 100:
        config.walk_speed_right = 100
    elif config.line_right_speed + PIDvalue < config.min_right_speed:
        config.walk_speed_right = 0
    else:
        config.walk_speed_right = config.line_right_speed + PIDvalue

    config.previous_error = config.line_error
    time.sleep(0.001)


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_read)

config.walk_speed_left = 40
config.walk_speed_right = 44
config.drive_left.start(config.walk_speed_left)
config.drive_right.start(config.walk_speed_right)

counter = 0

while config.walk_running:
    counter += 1
    # if counter == 10:
    #     config.walk_running = False
    #print("Line {}".format(counter))

    follow_line()

    config.drive_left.ChangeDutyCycle(config.walk_speed_left)
    config.drive_right.ChangeDutyCycle(config.walk_speed_right)

    if config.obstacle_number > -1:
        print("Found obstacle", config.obstacle_number)
    time.sleep(0.001)

    #distance_left = measure_distance(config.ultrasonic_pin1)
    #print("Left :", distance_left)


print(config.obstacle_number)

#time.sleep(2)
#rfid.terminate()
#distance.terminate()
#follower.terminate()

