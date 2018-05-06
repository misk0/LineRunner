import config
from RPi import GPIO
from threading import Thread
#from gpiozero import PWMOutputDevice
import time
import RFIDReader
import FollowMeBaby
import FoundInSpace

config.init()

#GPIO.setmode(GPIO.BOARD)

# Create thread for RFID reading
rfid = RFIDReader.RFIDReader()
rfidThread = Thread(target=rfid.run)
rfidThread.start()

# Create thread for line following
# follower = FollowMeBaby.FollowMeBaby()
# followerThread = Thread(target=follower.run)
# followerThread.start()

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

driveLeft = GPIO.PWM(config.left_motor_pwm, 100)
driveRight = GPIO.PWM(config.right_motor_pwm, 100)

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
GPIO.setup(config.ultrasonic_trigger_pin, GPIO.OUT)
GPIO.setup(config.ultrasonic_pin1, GPIO.IN)
GPIO.setup(config.ultrasonic_pin2, GPIO.IN)
GPIO.setup(config.ultrasonic_pin3, GPIO.IN)


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


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
config.walk_speed_left = 30
config.walk_speed_right = 32
driveLeft.start(config.walk_speed_left)
driveRight.start(config.walk_speed_right)

counter = 0

while config.walk_running:
    counter += 1
    if counter == 10:
        config.walk_running = False
    #print("Line {}".format(counter))
    time.sleep(0.5)

    driveLeft.ChangeDutyCycle(config.walk_speed_left)
    driveRight.ChangeDutyCycle(config.walk_speed_right)

    distance_left = measure_distance(config.ultrasonic_pin1)
    print("Left :", distance_left)


print(config.obstacle_number)
driveLeft.stop()
driveRight.stop()

rfid.terminate()
#distance.terminate()
#follower.terminate()

