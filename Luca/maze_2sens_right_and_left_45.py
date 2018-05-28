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

    dist_right = Distance.measure_distance(config.ultrasonic_triggers[config.US_CENTER], debug=False)
    dist_left = Distance.measure_distance(config.ultrasonic_triggers[config.US_LEFT], debug=False)

    #RIGHT
    if (dist_right >= 21):
        Right_Direction = True
        Right_Duty = 100
        Right_delay = 100
    elif (dist_right >= 17):
        Right_Direction = True
        Right_Duty = 80
        Right_delay = 200
    elif (dist_right >= 13):
        Right_Direction = True
        Right_Duty = 60
        Right_delay = 250
    elif (dist_right >= 9):
        Right_Direction = True
        Right_Duty = 45
        Right_delay = 350
    elif (dist_right >= 6):
        Right_Direction = False
        Right_Duty = 0
        Right_delay = 500
    elif (dist_right >= 3):
        Right_Direction = False
        Right_Duty = 50;
        Right_delay = 350
    else:
        Right_Direction = False
        Right_Duty = 80
        Right_delay = 150

#Left
    if (dist_left >= 21):
        Left_Direction = True
        Left_Duty = 100
        Left_delay = 100
    elif (dist_left >= 17):
        Left_Direction = True
        Left_Duty = 80
        Left_delay = 200
    elif (dist_left >= 13):
        Left_Direction = True
        Left_Duty = 60
        Left_delay = 250
    elif (dist_left >= 9):
        Left_Direction = True
        Left_Duty = 45
        Left_delay = 350
    elif (dist_left >= 6):
        Left_Direction = False
        Left_Duty = 0
        Left_delay = 500
    elif (dist_left >= 3):
        Left_Direction = False
        Left_Duty = 50;
        Left_delay = 350
    else:
        Left_Direction = False
        Left_Duty = 80
        Left_delay = 150

    if (Right_Direction == False and Left_Direction == False):
        config.drive_left.ChangeDutyCycle(0)
        config.drive_right.ChangeDutyCycle(0)
        GPIO.output(config.left_motor_direction, GPIO.HIGH)
        GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
        GPIO.output(config.right_motor_direction, GPIO.LOW)
        GPIO.output(config.right_motor_direction_inv, GPIO.HIGH)
        config.drive_left.ChangeDutyCycle(50)
        config.drive_right.ChangeDutyCycle(50)
        time.sleep(3) #time needed to turn 180°
        config.drive_left.ChangeDutyCycle(0)
        config.drive_right.ChangeDutyCycle(0)
        GPIO.output(config.left_motor_direction, GPIO.HIGH)
        GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
        GPIO.output(config.right_motor_direction, GPIO.HIGH)
        GPIO.output(config.right_motor_direction_inv, GPIO.LOW)
    else:
        if (Right_Direction == False):
            config.drive_right.ChangeDutyCycle(0)
            GPIO.output(config.right_motor_direction, GPIO.LOW)
            GPIO.output(config.right_motor_direction_inv, GPIO.HIGH)
        if (Left_Direction == False):
            config.drive_left.ChangeDutyCycle(0)
            GPIO.output(config.left_motor_direction, GPIO.LOW)
            GPIO.output(config.left_motor_direction_inv, GPIO.HIGH)

        config.drive_left.ChangeDutyCycle(Left_Duty)
        config.drive_right.ChangeDutyCycle(Right_Duty)
        if (Left_delay > Right_delay):
            time.sleep(Left_delay)
        else:
            time.sleep(Right_delay)

        if (Right_Direction == False):
            config.drive_right.ChangeDutyCycle(0)
            GPIO.output(config.right_motor_direction, GPIO.HIGH)
            GPIO.output(config.right_motor_direction_inv, GPIO.LOW)
        if (Left_Direction == False):
            config.drive_left.ChangeDutyCycle(0)
            GPIO.output(config.left_motor_direction, GPIO.HIGH)
            GPIO.output(config.left_motor_direction_inv, GPIO.LOW)

# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_read)

config.drive_left.start(config.walk_speed_left)
config.drive_right.start(config.walk_speed_right)

while True:
    loop()
