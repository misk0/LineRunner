import RPi.GPIO as GPIO
from gpiozero import PWMOutputDevice
from time import sleep

# GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use
                          # Broadcom SOC channel names.

# GPIO.setup(16, GPIO.OUT)  # Set GPIO pin 12 to output mode.
print("Start")
driveLeft = PWMOutputDevice(23, True, 1, 1000)
forwardLeft = PWMOutputDevice(27)
forwardLeft2 = PWMOutputDevice(22)

driveLeft.value = 0.5
forwardLeft.value = True
forwardLeft2.value = True

# pwm = GPIO.PWM(16, 1000)   # Initialize PWM on pwmPin 100Hz frequency
# dc=0                               # set dc variable to 0 for 0%
# pwm.start(dc)                      # Start PWM with 0% duty cycle
# pwm.ChangeDutyCycle(50)
sleep(40)
# GPIO.cleanup()
