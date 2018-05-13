# Variables
def init():
    # when True robot should move
    global walk_running
    walk_running = True

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

    # When True line following method should be used to guide robot movement
    global  follow_the_line
    follow_the_line = True

    # Value indicate which obstacle is recognized. Usually set by RFID sensor
    # 1 - Simple Labyrinth
    # 2 - Complex Labyrinth
    # 3 - Ninepins (birilli)
    # 4 - Trapeze
    # 5 - Chessboard
    # 6 - Wreckage (macerie)
    # 7 - Stairs
    # 8 - Drone
    global obstacle_number
    obstacle_number = -1
    global inside_obstacle
    inside_obstacle = False


# * * * * * * * * * * * *  CONSTANTS * * * * * * * * * * * * * * * *
max_left_speed = 54
max_right_speed = 60

obstacle_list = ["labyrinth-simple", "labyrinth-complex", "ninepins", "trapeze", "chessboard", "wreckage",
                 "stairs", "drone"]
obstacle_start = [10, 20, 30, 40, 50, 60, 70, 80]
obstacle_end = [(11, 12, 13, 14), (21, 22, 23, 24), (31, 32, 33, 34), (41, 42, 43, 44), (51, 52, 53, 54),
                (61, 62, 63, 64), (71, 72, 73, 74), (81, 82, 83, 84)]



# PIN configuration - GPIO number (not PIN)
# Motor1 - right
right_motor_pwm = 3
right_motor_direction = 5
right_motor_direction_inv = 7
# Motor2 - right
left_motor_pwm = 11
left_motor_direction = 8
left_motor_direction_inv = 10

# RFID config
rfid_mosi = 19
rfid_miso = 21
rfid_rst = 22
rfid_sck = 23
rfid_sda = 24

# Ultrasonic sensors
US_LEFT = 0
US_CENTER = 1
US_RIGHT = 2
ultrasonic_pins = [31, 32, 33]
ultrasonic_triggers = [13, 15, 16]

# Line follow sensors
line_follow_pin1 = 35
line_follow_pin2 = 36
line_follow_pin3 = 37
line_follow_pin4 = 38
line_follow_pin5 = 40
