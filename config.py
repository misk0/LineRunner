# Variables
def init():
    # when True robot should move
    # global walk_running
    # walk_running = True

    # Automatic means motors should be running continuously
    # When False, encoder should be read and tracker should move only with certain number of rotation
    global walk_mode_automatic
    walk_mode_automatic = True

    # Speed of left tracker
    global walk_speed_left
    walk_speed_left = max_left_speed
    # Speed of right tracker
    global walk_speed_right
    walk_speed_right = max_right_speed

    global drive_left
    global drive_right

    global LastRFID

    # When True line following method should be used to guide robot movement
    # global  follow_the_line
    # follow_the_line = True

    # Value indicate which obstacle is recognized. Usually set by RFID sensor
    # 1 - Simple Labyrinth
    # 2 - Complex Labyrinth
    # 3 - Ninepins (birilli)
    # 4 - Trapeze
    # 5 - Chessboard
    # 6 - Wreckage (macerie)
    # 7 - Stairs
    # 8 - Drone
    # global obstacle_number
    # obstacle_number = -1
    # global inside_obstacle
    # inside_obstacle = False

    #Line follow variables
    global previous_error
    previous_error = 0

    # global line_integrative
    # line_integrative = 0

    global line_error
    line_error = 0

    global dist_error
    dist_error = 0
    
    # global dist_integrative
    # dist_integrative = 0
    
    global dist_previous_error
    dist_previous_error = 0

    global previous_dist_left
    previous_dist_left = 0

    global dist_count
    dist_count = 10
    
# * * * * * * * * * * * *  CONSTANTS * * * * * * * * * * * * * * * *
max_left_speed = 54
max_right_speed = 60

line_left_speed = 55#60
line_right_speed = 53#58

min_left_speed = 37
min_right_speed = 35

line_kp = 15
line_kd = 20
line_ki = 0
#
# Distance_MinValue = 10

dist_kp = 15
dist_kd = 20
dist_ki = 0

dist_left_speed = 50
dist_right_speed = 48


obstacle_list = ["labyrinth-simple", "labyrinth-complex", "ninepins", "trapeze", "chessboard", "wreckage",
                 "stairs", "drone"]
obstacle_start = [("e5788628"), ("3fc84729"), ("30"), ("40"), ("50"), ("60"), ("70"), ("80")]
obstacle_end_left = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44, 51, 52, 53, 54]
obstacle_end_right = [61, 62, 63, 64, 71, 72, 73, 74, 81, 82, 83, 84]



# PIN configuration - PIN number

#miscellaneous
program_switch = 3

en_shoot = 16

# Ultrasonic sensors
US_LEFT = 1
# US_CENTER = 1
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