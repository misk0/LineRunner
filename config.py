# Variables
def init():

    # Automatic means motors should be running continuously
    # When False, encoder should be read and tracker should move only with certain number of rotation
    # global walk_mode_automatic
    # walk_mode_automatic = True

    # Speed of left tracker
    global walk_speed_left
    walk_speed_left = 60
    # Speed of right tracker
    global walk_speed_right
    walk_speed_right = 60

    global drive_left
    global drive_right

    global LastRFID

    #servo
    global servo_pwm


    #SimpleMaze
    global SimpleMazeCount
    SimpleMazeCount = 10

    global PreviousDistLeft_SimpleMaze
    PreviousDistLeft_SimpleMaze = 0

    global SimpleMazeSpeed
    SimpleMazeSpeed = 45

    global EndSimpleMaze
    EndSimpleMaze = False

    global SimpleMazeLeftDone
    SimpleMazeLeftDone = False

    global SimpleMazeError
    SimpleMazeError = 0

    global SimpleMazePrevError
    SimpleMazePrevError = 0

    #Ninepins
    global EndNinepins
    EndNinepins = False

    global NinepinsFirsTime
    NinepinsFirsTime = False

    global NinepinsFinalPart
    NinepinsFinalPart = False

    global NinepinsFinalError
    NinepinsFinalError = 0

    global NinepinsFinalPrevError
    NinepinsFinalPrevError = 0

    global NinepinsCount
    NinepinsCount = 10

    global NinepinsPrevLeft
    NinepinsPrevLeft = 0

    global NinepinsError
    NinepinsError = 0

    global NinepinsPrevError
    NinepinsPrevError = 0

    #Steps
    global StepsFirstTime
    StepsFirstTime = False

    global StepsEndedFirstTime
    StepsEndedFirstTime = True

    global EndSTeps
    EndSTeps = False

    global StepCount
    StepCount = 10

    global StepPrevRight
    StepPrevRight = 0

    global StepError
    StepError = 0

    global StepsFinalError
    StepsFinalError = 0

    global StepsFinalPrevError
    StepsFinalPrevError = 0

    #Line
    global line_error
    line_error = 0

    global previous_error
    previous_error = 0

    #Ramp
    global EndRamp
    EndRamp = False

    global RampFirstTime
    RampFirstTime = False

    global RampEndedFirstTime
    RampEndedFirstTime = True

    global RampCount
    RampCount = 10

    global RampPrevRight
    RampPrevRight = 0

    global RampError
    RampError = 0

    global RampFinalError
    RampFinalError = 0

    global RampFinalPrevError
    RampFinalPrevError = 0

    #Rubble
    global EndRubble
    EndRubble = False

    global RubbleFirstTime
    RubbleFirstTime = False

    global RubbleEndedFirstTime
    RubbleEndedFirstTime = True

    global RubbleCount
    RubbleCount = 10

    global RubblePrevRight
    RubblePrevRight = 0

    global RubbleError
    RubbleError = 0

    global RubbleFinalError
    RubbleFinalError = 0

    global RubbleFinalPrevError
    RubbleFinalPrevError = 0





    # global AlreadyDone
    # AlreadyDone = False

    #Line follow variables


    # global line_integrative
    # line_integrative = 0



    # global dist_error
    # dist_error = 0

    # global speed
    # speed = 45


    # global dist_integrative
    # dist_integrative = 0
    
    # global dist_previous_error
    # dist_previous_error = 0

    # global previous_dist_left
    # previous_dist_left = 0
    # global pervious_dist_right
    # pervious_dist_right = 0

    # global dist_count
    # dist_count = 10


    # global endNine
    # endNine = False



# * * * * * * * * * * * *  CONSTANTS * * * * * * * * * * * * * * * *
#Ninepins
NinepinsFinalLeftSpeed = 50
NinepinsFinalRightSpeed = 50

NinepinsLeftSpeed = 50
NinepinsRightSpeed = 50

#Steps
StepLeftSpeed = 50
StepRightSpeed = 50

StepsFinalLeftSpeed = 50
StepsFinalRightSpeed = 50

#Line
# line_kp = 25
# line_kd = 15
line_kp = 11
line_kd = 4
# line_ki = 0

line_left_speed = 45#60
line_right_speed = 45#58

#Ramp
RampLeftSpeed = 50
RampRightSpeed = 50

RampFinalLeftSpeed = 50
RampFinalRightSpeed = 50

#Rubble
RubbleLeftSpeed = 50
RubbleRightSpeed = 50

RubbleFinalLeftSpeed = 50
RubbleFinalRightSpeed = 50



# max_left_speed = 54
# max_right_speed = 60



min_left_speed = 37
min_right_speed = 35


#
# Distance_MinValue = 10
# simplemaze
# dist_kp = 5
# dist_kd = 20
# dist_ki = 0
# dist_left_speed = 50
# dist_right_speed = 48

#steps
# dist_kp = 15
# dist_kd = 20
# dist_ki = 0

# dist_left_speed = 75
# dist_right_speed = 75


obstacle_list = ["labyrinth-simple", "labyrinth-complex", "ninepins", "trapeze", "chessboard", "wreckage",
                 "stairs", "drone"]
obstacle_start = [("35d68628"), (""), ("c529fb35"), ("b397fa35"), ("b715665"), ("e7f6f735"), ("b397fa35"), ("c7c7d65")]
obstacle_end_left = ["84fa4412", "bbc426d3", "95a78628", "25afc928", 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44, 51, 52, 53, 54]
obstacle_end_right = ["8565884", "55e3834", "e5ed884", 64, 71, 72, 73, 74, 81, 82, 83, 84]



# PIN configuration - PIN number

#miscellaneous
servo = 3
calib = 5
en_shoot = 16

# Ultrasonic sensors
US_LEFT = 1
US_CENTER = 0
US_RIGHT = 2
ultrasonic_triggers = [26, 7, 29]
ultrasonic_echo = [32, 33, 31]

# Motor right
right_motor_pwm = 11
right_motor_direction = 15
right_motor_direction_inv = 10

# Motor left
left_motor_pwm = 13
left_motor_direction = 8
left_motor_direction_inv = 12

# Line follow sensors
line_follow_lmax = 36
line_follow_lmin = 38
line_follow_mid = 40
line_follow_rmin = 37
line_follow_rmax = 35

# RFID config
# rfid_mosi = 19
# rfid_miso = 21
# rfid_rst = 22
# rfid_sck = 23
# rfid_sda = 24
