# when True robot should move
walk_running = True

# Automatic means motors should be running continuously
# When False, encoder should be read and tracker should move only with certain number of rotation
walk_mode_automatic = True

# Robot speed
# If negative, robot should go to the back
walk_speed = 100

# Speed of left tracker
walk_speed_left = 100
# Speed of right tracker
walk_speed_right = 100

# represent the ratio between left and right tracker speed
# -90 is full left, 0 is straight, 90 is full right
walk_angle = 0

# When True line following method should be used to guide robot movement
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
obstacle_number = 0

# PIN configuration - GPIO number (not PIN)
# Motor1 - left
left_encoder = 17
left_motor_pwm = 23
left_motor_direction = 27
# Motor2 - right
right_encoder = 18
right_motor_pwm = 24
right_motor_direction = 22

# RFID config
rfid_mosi = 19
rfid_miso = 21
rfid_rst = 22
rfid_sck = 23
rfid_sda = 24

