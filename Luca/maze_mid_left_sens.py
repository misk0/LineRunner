import Distance
import config
from RPi import GPIO
import time
import signal
import sys

config.init()

GPIO.setup(config.left_motor_pwm, GPIO.OUT)
GPIO.setup(config.left_motor_direction, GPIO.OUT)
GPIO.setup(config.left_motor_direction_inv, GPIO.OUT)
GPIO.setup(config.right_motor_pwm, GPIO.OUT)
GPIO.setup(config.right_motor_direction, GPIO.OUT)
GPIO.setup(config.right_motor_direction_inv, GPIO.OUT)

config.drive_left = GPIO.PWM(config.left_motor_pwm, 100)
config.drive_right = GPIO.PWM(config.right_motor_pwm, 100)

GPIO.setup(config.ultrasonic_triggers[config.US_LEFT], GPIO.OUT)
GPIO.setup(config.ultrasonic_triggers[config.US_CENTER], GPIO.OUT)
GPIO.setup(config.ultrasonic_triggers[config.US_RIGHT], GPIO.OUT)
GPIO.setup(config.ultrasonic_pins[config.US_LEFT], GPIO.IN)
GPIO.setup(config.ultrasonic_pins[config.US_CENTER], GPIO.IN)
GPIO.setup(config.ultrasonic_pins[config.US_RIGHT], GPIO.IN)

GPIO.output(config.left_motor_direction, GPIO.HIGH)
GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
GPIO.output(config.right_motor_direction, GPIO.HIGH)
GPIO.output(config.right_motor_direction_inv, GPIO.LOW)


def end_read(signal, frame):
    print("\nCtrl+C captured, ending read.")
    config.drive_left.stop()
    config.drive_right.stop()
    GPIO.cleanup()
    sys.exit()


def loop():
    dist_mid = Distance.measure_distance(config.ultrasonic_triggers[config.US_CENTER], debug=False)
    dist_left = Distance.measure_distance(config.ultrasonic_triggers[config.US_LEFT], debug=False)

    if (dist_left < 7):
        Left_sens = True
    else:
        Left_sens = False

    if (dist_mid < 7):
        Mid_sens = True
    else:
        Mid_sens = False

    if (Mid_sens == False and Left_sens == False):
    #    slow left and fast right
        config.drive_left.ChangeDutyCycle(max_left_speed - 15)
        config.drive_right.ChangeDutyCycle(max_right_speed + 15)

    if (Mid_sens == False and Left_sens == True):
        #go FW
        config.drive_left.ChangeDutyCycle(max_left_speed)
        config.drive_right.ChangeDutyCycle(max_right_speed)

    if (Mid_sens == True and Left_sens == True):
        #fast left slow right
        config.drive_left.ChangeDutyCycle(max_left_speed + 15)
        config.drive_right.ChangeDutyCycle(max_right_speed - 15)

    if (Mid_sens == True and Left_sens == False):
        #stop left and fast right
        config.drive_left.ChangeDutyCycle(0)
        config.drive_right.ChangeDutyCycle(max_right_speed + 15)


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_read)

config.drive_left.start(config.walk_speed_left)
config.drive_right.start(config.walk_speed_right)

while True:
    loop()
