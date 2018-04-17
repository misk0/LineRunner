# when True robot should move
walk_running = True

# Automatic means motors should be running continuously
# When False, encoder should be read and tracker should move only with certain number of rotation
walk_mode_automatic = True

# Speed of left tracker
walk_speed_left = 100
# Speed of right tracker
walk_speed_right = 100

# represent the ratio between left and right tracker speed
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


