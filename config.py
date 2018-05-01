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
    walk_speed_left = 0
    # Speed of right tracker
    global walk_speed_right
    walk_speed_right = 0

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


# * * * * * * * * * * * *  CONSTANTS * * * * * * * * * * * * * * * *
# PIN configuration - GPIO number (not PIN)
# Motor1 - left
left_encoder = 17
left_motor_pwm = 23
left_motor_direction = 27
left_motor_direction_inv = 27
# Motor2 - right
right_encoder = 18
right_motor_pwm = 24
right_motor_direction = 22
right_motor_direction_inv = 22

# RFID config
rfid_mosi = 19
rfid_miso = 21
rfid_rst = 22
rfid_sck = 23
rfid_sda = 24

