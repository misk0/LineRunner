import config
from RPi import GPIO
from threading import Thread
import time
import RFIDReader
import signal
import end_program
import Line
import MAzeNew
import SimpleMaze
import ComplexMaze
import Step
import Ramp
import Rubble
import Drone
import Ninepins
import Basket
import NinepinsFinal
import RampFinal
import StepsFinal
import RubbleFinal

GPIO.cleanup()

#Initialize global variables
config.init()

GPIO.setmode(GPIO.BOARD)

# Create thread for RFID reading
rfid = RFIDReader.RFIDReader()
rfidThread = Thread(target=rfid.run)
rfidThread.start()

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
# GPIO.setup(config.ultrasonic_triggers[config.US_CENTER], GPIO.OUT)
# GPIO.setup(config.ultrasonic_echo[config.US_CENTER], GPIO.IN)
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


# * * * * * * * * * * * * * * * * * * * * * * * * * *
# Main program
# * * * * * * * * * * * * * * * * * * * * * * * * * *
signal.signal(signal.SIGINT, end_program.end_read)

config.walk_speed_left = 40
config.walk_speed_right = 40
config.drive_left.start(config.walk_speed_left)
config.drive_right.start(config.walk_speed_right)

config.LastRFID = " "

GPIO.output(config.en_shoot,GPIO.LOW)

while True:
    if config.LastRFID == "labyrinth-simple":
        if config.EndSimpleMaze == True:
            if GPIO.input(config.line_follow_lmax) or GPIO.input(config.line_follow_lmin) or GPIO.input(config.line_follow_mid) or GPIO.input(config.line_follow_rmin) or GPIO.input(config.line_follow_rmax):
                config.LastRFID = ""
        MAzeNew.follow_distance(False)
        config.drive_left.ChangeDutyCycle(config.walk_speed_left)
        config.drive_right.ChangeDutyCycle(config.walk_speed_right)
    # elif config.LastRFID == "labyrinth-complex":
    #     ComplexMaze.ComplexMaze()
    # elif config.LastRFID == "drone":
    #     Drone.Drone()
    # elif config.LastRFID == "chessboard":
    #     Basket.Basket()
    #     # config.AlreadyDone = True
    #     # config.drive_left.ChangeDutyCycle(0)
    #     # config.drive_right.ChangeDutyCycle(0)
    #     SimpleMaze.SimpleMaze()
    #     # GPIO.output(config.en_shoot, GPIO.HIGH)
    #     # time.sleep(2)
    #     # GPIO.output(config.en_shoot, GPIO.LOW)
    #     # config.LastRFID == ""
    #     # config.drive_left.ChangeDutyCycle(40)
    #     # config.drive_right.ChangeDutyCycle(40)
    #     # time.sleep(3)
    #     # config.AlreadyDone = False
    elif config.LastRFID == "ninepins":
        if config.EndNinepins == True:
            if GPIO.input(config.line_follow_lmax) or GPIO.input(config.line_follow_lmin) or GPIO.input(config.line_follow_mid) or GPIO.input(config.line_follow_rmin) or GPIO.input(config.line_follow_rmax):
                config.LastRFID = ""
        if config.NinepinsFirsTime == False:
            config.NinepinsFirsTime = True
            config.drive_left.ChangeDutyCycle(60)
            config.drive_right.ChangeDutyCycle(60)
            time.sleep(0.5)
            NinepinsTime1 = time.time()
            config.EndNinepins = True
        # print("time",time.time() - TimeFirst)
        if config.NinepinsFinalPart == False:
            if time.time() - NinepinsTime1 < 0.8:
                Ninepins.Ninepins(False)
                config.drive_left.ChangeDutyCycle(config.walk_speed_left)
                config.drive_right.ChangeDutyCycle(config.walk_speed_right)
            else:
                config.drive_left.ChangeDutyCycle(65)
                config.drive_right.ChangeDutyCycle(82)
                time.sleep(2.2)
                NinepinsTime1 = time.time()
                config.NinepinsFinalPart = True
        else:
            NinepinsFinal.follow_distance(False)
            config.drive_left.ChangeDutyCycle(config.walk_speed_left)
            config.drive_right.ChangeDutyCycle(config.walk_speed_right)

    elif config.LastRFID == "trapeze":
        if config.EndRamp == True:
            if GPIO.input(config.line_follow_lmax) or GPIO.input(config.line_follow_lmin) or GPIO.input(
                    config.line_follow_mid) or GPIO.input(config.line_follow_rmin) or GPIO.input(
                    config.line_follow_rmax):
                config.LastRFID = ""
        if config.RampFirstTime == False:
            RampTime1 = time.time()
            config.RampFirstTime = True
        print("time",time.time() - RampTime1)
        if time.time() - RampTime1 <= 2.5:
            Ramp.Ramp(False)
            config.drive_left.ChangeDutyCycle(config.walk_speed_left)
            config.drive_right.ChangeDutyCycle(config.walk_speed_right)
        elif time.time() - RampTime1 > 2.5 and time.time() - RampTime1 <= 4:
            config.drive_left.ChangeDutyCycle(60)
            config.drive_right.ChangeDutyCycle(80)
        else:
            RampFinal.follow_distance(False)
            config.drive_left.ChangeDutyCycle(config.walk_speed_left)
            config.drive_right.ChangeDutyCycle(config.walk_speed_right)
            config.EndRamp = True

    elif config.LastRFID == "wreckage":
        if config.EndRubble == True:
            if GPIO.input(config.line_follow_lmax) or GPIO.input(config.line_follow_lmin) or GPIO.input(
                    config.line_follow_mid) or GPIO.input(config.line_follow_rmin) or GPIO.input(
                    config.line_follow_rmax):
                config.LastRFID = ""
        if config.RubbleFirstTime == False:
            RubbleTime1 = time.time()
            config.RubbleFirstTime = True
        print("time",time.time() - RampTime1)
        if time.time() - RubbleTime1 <= 2.5:
            Rubble.Rubble(False)
            config.drive_left.ChangeDutyCycle(config.walk_speed_left)
            config.drive_right.ChangeDutyCycle(config.walk_speed_right)
        elif time.time() - RubbleTime1 > 2.5 and time.time() - RubbleTime1 <= 4:
            config.drive_left.ChangeDutyCycle(60)
            config.drive_right.ChangeDutyCycle(80)
        else:
            RubbleFinal.follow_distance(False)
            config.drive_left.ChangeDutyCycle(config.walk_speed_left)
            config.drive_right.ChangeDutyCycle(config.walk_speed_right)
            config.EndRubble = True

    elif config.LastRFID == "stairs":
        if config.EndSteps == True:
            if GPIO.input(config.line_follow_lmax) or GPIO.input(config.line_follow_lmin) or GPIO.input(
                    config.line_follow_mid) or GPIO.input(config.line_follow_rmin) or GPIO.input(
                    config.line_follow_rmax):
                config.LastRFID = ""
        if config.StepsFirstTime == False:
            StepsTime1 = time.time()
            config.StepsFirstTime = True
        print("time",time.time() - StepsTime1)
        if time.time() - StepsTime1 <= 2.5:
            Step.Step(False)
            config.drive_left.ChangeDutyCycle(config.walk_speed_left)
            config.drive_right.ChangeDutyCycle(config.walk_speed_right)
        elif time.time() - StepsTime1 > 2.5 and time.time() - StepsTime1 <= 4:
            config.drive_left.ChangeDutyCycle(60)
            config.drive_right.ChangeDutyCycle(80)
        else:
            StepsFinal.follow_distance(False)
            config.drive_left.ChangeDutyCycle(config.walk_speed_left)
            config.drive_right.ChangeDutyCycle(config.walk_speed_right)
            config.EndSteps = True
        # PID_final_maze.follow_distance(False)
    else:
    #     if config.LastRFID == "obstacle_end_left":
    #         #muovi leggermente a destra
    #         config.LastRFID = "taguscitacentrale"
    #         print("RFID END LEFT")
    #     if config.LastRFID == "obstacle_end_right":
    #         #muovi leggermente a sinistra
    #         config.LastRFID = "taguscitacentrale"
    #         print("RFID END RIGHT")

        # print("Line Follower")
        #segui linea
        Line.follow_line(False)
    # Rubble.Rubble()

    # FollowMeBaby.FollowMe()
        config.drive_left.ChangeDutyCycle(config.walk_speed_left)
        config.drive_right.ChangeDutyCycle(config.walk_speed_right)
        # print(config.walk_speed_left)
        time.sleep(0.1)
        config.drive_left.ChangeDutyCycle(0)
        config.drive_right.ChangeDutyCycle(0)




    # if (GPIO.input(config.program_switch)==0):
    #     print("low")
    # if (GPIO.input(config.program_switch)==1):
    #     print("high")
    # Distance.follow_distance(debug=True)
    # print("right",Distance.measure_distance(config.US_RIGHT))
    # print("left",Distance.measure_distance(config.US_CENTER))
    # if config.obstacle_number > -1:
    #     print("Found obstacle", config.obstacle_number)
    #     print(config.obstacle_number)
    # else:
    #     Line.follow_line(False)
    # config.drive_left.ChangeDutyCycle(config.walk_speed_left)
    # config.drive_right.ChangeDutyCycle(config.walk_speed_right)
    # time.sleep(0.05)
    # config.drive_left.ChangeDutyCycle(0)
    # config.drive_right.ChangeDutyCycle(0)




