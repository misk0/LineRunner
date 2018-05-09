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
    obstacle_number = 0


max_left_speed = 54
max_right_speed = 60

# * * * * * * * * * * * *  CONSTANTS * * * * * * * * * * * * * * * *
# PIN configuration - GPIO number (not PIN)
# Motor1 - left
#right_encoder = 11
right_motor_pwm = 16
right_motor_direction = 13
right_motor_direction_inv = 8
# Motor2 - right
#left_encoder = 12
left_motor_pwm = 12
left_motor_direction = 15
left_motor_direction_inv = 10

# RFID config
rfid_mosi = 19
rfid_miso = 21
rfid_rst = 22
rfid_sck = 23
rfid_sda = 24

# Ultrasonic sensors
ultrasonic_pin1 = 29
ultrasonic_pin2 = 31
ultrasonic_pin3 = 32
ultrasonic_trigger_pin = 40

# Line follow sensors
line_follow_pin1 = 33
line_follow_pin2 = 35
line_follow_pin3 = 26
line_follow_pin4 = 37
line_follow_pin5 = 38
