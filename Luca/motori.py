import RPi.GPIO as GPIO  # Import the GPIO library.
import time  # Import time library


GPIO.setmode(GPIO.BCM)  # Set Pi to use pin number when referencing GPIO pins.

GPIO.setup(23, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(24, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(27, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(22, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(14, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(15, GPIO.OUT)  # Set GPIO pin 12 to output mode.

pwm1 = GPIO.PWM(23, 100)  # Initialize PWM on pwmPin 100Hz frequency
pwm2 = GPIO.PWM(24, 100)  # Initialize PWM on pwmPin 100Hz frequency



dc = 0  # set dc variable to 0 for 0%

pwm1.start(dc)  # Start PWM with 0% duty cycle
pwm2.start(dc)  # Start PWM with 0% duty cycle


GPIO.output(27, True)
GPIO.output(14, False)
GPIO.output(22, True)
GPIO.output(15, False)

pwm1.ChangeDutyCycle(75)
pwm2.ChangeDutyCycle(67)

time.sleep(3.5)

pwm1.stop()
pwm2.stop()
GPIO.cleanup()  # resets GPIO ports used back to input mode