import config
from RPi import GPIO
import time
import signal
import end_program
import GoParallel
import MAzeNew
import PID_final_maze
import Distance
import provaMaze


#Initialize global variables
config.init()

GPIO.setmode(GPIO.BOARD)

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
config.drive_left = GPIO.PWM(config.left_motor_pwm, 200)
config.drive_right = GPIO.PWM(config.right_motor_pwm, 200)

GPIO.output(config.left_motor_direction, GPIO.HIGH)
GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
GPIO.output(config.right_motor_direction, GPIO.HIGH)
GPIO.output(config.right_motor_direction_inv, GPIO.LOW)


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_program.end_read)

GPIO.output(config.en_shoot,GPIO.LOW)


# config.walk_speed_left = 0
# config.walk_speed_right = 0
config.drive_left.start(40)
config.drive_right.start(40)

#provare FW
# config.drive_left.ChangeDutyCycle(65)
# config.drive_right.ChangeDutyCycle(82)

#provare soft left
# config.drive_left.ChangeDutyCycle(55)
# config.drive_right.ChangeDutyCycle(90)

#provare soft right
# config.drive_left.ChangeDutyCycle(75)
# config.drive_right.ChangeDutyCycle(75)

#provare semi soft left
# config.drive_left.ChangeDutyCycle(50)
# config.drive_right.ChangeDutyCycle(100)

# provare semi soft right
# config.drive_left.ChangeDutyCycle(100)
# config.drive_right.ChangeDutyCycle(60)

#provare hard left
# config.drive_left.ChangeDutyCycle(0)
# config.drive_right.ChangeDutyCycle(100)


#provare hard right
# config.drive_left.ChangeDutyCycle(100)
# config.drive_right.ChangeDutyCycle(0)


# ostacoli
# config.drive_left.ChangeDutyCycle(60)
# config.drive_right.ChangeDutyCycle(80)

# se c'è muro SX ma non front -> avanti
# se c'è muro Sx e anche front -> gira molto destra
# se non c'è muro SX e non front -> gira un po' sinistra
# se non c'è muro SX ma c'è front -> gira molto destra


while True:
    ciao = 1
    # PID_final_maze.follow_distance(True)
    # MAzeNew.follow_distance(False)
    # config.drive_left.ChangeDutyCycle(config.walk_speed_left)
    # config.drive_right.ChangeDutyCycle(config.walk_speed_right)

