import time
from pololu_drv8835_rpi import motors, MAX_SPEED


#test_forward_speeds = list(range(MAX_SPEED, 0, -1)) 
test_forward_speeds = MAX_SPEED

try:
    motors.setSpeeds(0)
    print("Motor 2 forward")
    #for s in test_forward_speeds:
    motors.motor2.setSpeed(test_forward_speeds)
    time.sleep(10)

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
  motors.setSpeeds(0)
