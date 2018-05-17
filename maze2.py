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
    dist_right = Distance.measure_distance(config.ultrasonic_triggers[config.US_RIGHT], debug=False)

    if (dist_left > 8):
        config.drive_left.ChangeDutyCycle(max_left_speed)
        config.drive_right.ChangeDutyCycle(max_right_speed + 20)
    elif (dist_mid > 8):
        config.drive_left.ChangeDutyCycle(max_left_speed)
        config.drive_right.ChangeDutyCycle(max_right_speed)
    elif (dist_right > 8):
        config.drive_left.ChangeDutyCycle(max_left_speed + 20)
        config.drive_right.ChangeDutyCycle(max_right_speed)


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_read)

config.drive_left.start(config.walk_speed_left)
config.drive_right.start(config.walk_speed_right)

while True:
    loop()
