import config
from RPi import GPIO
from threading import Thread
import time
import RFIDReader
# import testRFID
# import FoundInSpace
import Distance
import FollowMeBaby
import signal
import end_program
import Line

#Initialize global variables
config.init()

# Create thread for RFID reading
rfid = RFIDReader.RFIDReader()
# rfid = testRFID.RFIDTest()
rfidThread = Thread(target=rfid.run)
rfidThread.start()


# GPIO.setmode(GPIO.BOARD)
#Initialize pins

#Program switch
GPIO.setup(config.program_switch, GPIO.IN)

#Shooter
GPIO.setup(config.en_shoot, GPIO.OUT)

#Distance sensors
#Left
GPIO.setup(config.ultrasonic_triggers[config.US_LEFT], GPIO.OUT)
GPIO.setup(config.ultrasonic_echo[config.US_LEFT], GPIO.IN)
#Mid
GPIO.setup(config.ultrasonic_triggers[config.US_CENTER], GPIO.OUT)
GPIO.setup(config.ultrasonic_echo[config.US_CENTER], GPIO.IN)
#Right
GPIO.setup(config.ultrasonic_triggers[config.US_RIGHT], GPIO.OUT)
GPIO.setup(config.ultrasonic_echo[config.US_RIGHT], GPIO.IN)

#Motor right
GPIO.setup(config.right_motor_pwm, GPIO.OUT)
GPIO.setup(config.right_motor_direction, GPIO.OUT)
GPIO.setup(config.right_motor_direction_inv, GPIO.OUT)

#Motor left
GPIO.setup(config.left_motor_pwm, GPIO.OUT)
GPIO.setup(config.left_motor_direction, GPIO.OUT)
GPIO.setup(config.left_motor_direction_inv, GPIO.OUT)

#Line sensors
GPIO.setup(config.line_follow_lmax, GPIO.IN)
GPIO.setup(config.line_follow_lmin, GPIO.IN)
GPIO.setup(config.line_follow_mid, GPIO.IN)
GPIO.setup(config.line_follow_rmin, GPIO.IN)
GPIO.setup(config.line_follow_rmax, GPIO.IN)


#Initialize motors
config.drive_left = GPIO.PWM(config.left_motor_pwm, 100)
config.drive_right = GPIO.PWM(config.right_motor_pwm, 100)

GPIO.output(config.left_motor_direction, GPIO.HIGH)
GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
GPIO.output(config.right_motor_direction, GPIO.HIGH)
GPIO.output(config.right_motor_direction_inv, GPIO.LOW)


# def measure_distance(sensor_pos, debug=False):
#     complex_distance = 0
#     retries = 0
#     pulse_start = 0
#     pulse_end = 0
#
#     for counter in range(3):
#         GPIO.output(config.ultrasonic_triggers[sensor_pos], GPIO.HIGH)
#         time.sleep(0.00001)
#         GPIO.output(config.ultrasonic_triggers[sensor_pos], GPIO.LOW)
#         while GPIO.input(config.ultrasonic_pins[sensor_pos]) == 0:
#             pulse_start = time.time()
#
#         while GPIO.input(config.ultrasonic_pins[sensor_pos]) == 1:
#             pulse_end = time.time()
#
#         pulse_duration = pulse_end - pulse_start
#         distance = pulse_duration * 17150
#         distance = round(distance, 2)
#
#         if debug:
#             print("Sensor : %s Current distance: %s" % (sensor_pos, distance))
#         if complex_distance == 0:
#             complex_distance = distance
#
#         if distance < complex_distance:
#             complex_distance = distance
#         time.sleep(0.05)
#
#     return complex_distance


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_program.end_read)

config.walk_speed_left = 0
config.walk_speed_right = 0
config.drive_left.start(config.walk_speed_left)
config.drive_right.start(config.walk_speed_right)

# ostacoli
# config.drive_left.ChangeDutyCycle(60)
# config.drive_right.ChangeDutyCycle(80)

GPIO.output(config.en_shoot,GPIO.HIGH)

while config.walk_running:

    # Line.follow_line(debug=False)
    # FollowMeBaby.FollowMe()
    # config.drive_left.ChangeDutyCycle(config.walk_speed_left)
    # config.drive_right.ChangeDutyCycle(config.walk_speed_right)
    loop = 1



    # if (GPIO.input(config.program_switch)==0):
    #     print("low")
    # if (GPIO.input(config.program_switch)==1):
    #     print("high")
    # Distance.follow_distance(debug=True)
    # print(Distance.measure_distance(config.US_RIGHT))

    if config.obstacle_number > -1:
        print("Found obstacle", config.obstacle_number)
        print(config.obstacle_number)




