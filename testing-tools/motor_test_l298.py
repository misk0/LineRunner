import RPi.GPIO as GPIO  # Import the GPIO library.
import time  # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.

GPIO.setup(33, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(13, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(8, GPIO.OUT)  # Set GPIO pin 12 to output mode.

pwm = GPIO.PWM(33, 5000)  # Initialize PWM on pwmPin 100Hz frequency
GPIO.output(13, True)
GPIO.output(8, False)

dc = 0  # set dc variable to 0 for 0%
pwm.start(dc)  # Start PWM with 0% duty cycle
pwm.ChangeDutyCycle(50)
time.sleep(15)

pwm.stop()
GPIO.cleanup()  # resets GPIO ports used back to input mode

# from gpiozero import PWMOutputDevice
# from gpiozero import DigitalOutputDevice
# from time import sleep
#
# # ///////////////// Define Motor Driver GPIO Pins /////////////////
# # Motor A, Left Side GPIO CONSTANTS
# PWM_DRIVE_LEFT = 23  # ENA - H-Bridge enable pin
# FORWARD_LEFT_PIN = 27  # IN1 - Forward Drive
# REVERSE_LEFT_PIN = 14  # IN2 - Reverse Drive
# # Motor B, Right Side GPIO CONSTANTS
# PWM_DRIVE_RIGHT = 24  # ENB - H-Bridge enable pin
# FORWARD_RIGHT_PIN = 22  # IN1 - Forward Drive
# REVERSE_RIGHT_PIN = 15  # IN2 - Reverse Drive
#
# # Initialise objects for H-Bridge GPIO PWM pins
# # Set initial duty cycle to 0 and frequency to 1000
# driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 5000)
# driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 5000)
#
# # Initialise objects for H-Bridge digital GPIO pins
# forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
# reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
# forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
# reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)
#
#
# def allStop():
#     forwardLeft.value = False
#     reverseLeft.value = True
#     forwardRight.value = False
#     reverseRight.value = True
#     driveLeft.value = 0
#     driveRight.value = 0
#
#
# def forwardDrive():
#     forwardLeft.value = False
#     reverseLeft.value = True
#     forwardRight.value = False
#     reverseRight.value = True
#     driveLeft.value = 0.2
#     driveRight.value = 0.2
#
#
# def reverseDrive():
#     forwardLeft.value = True
#     reverseLeft.value = False
#     forwardRight.value = True
#     reverseRight.value = False
#     driveLeft.value = 1.0
#     driveRight.value = 1.0
#
#
# def spinLeft():
#     forwardLeft.value = True
#     reverseLeft.value = False
#     forwardRight.value = False
#     reverseRight.value = True
#     driveLeft.value = 1.0
#     driveRight.value = 1.0
#
#
# def SpinRight():
#     forwardLeft.value = False
#     reverseLeft.value = True
#     forwardRight.value = True
#     reverseRight.value = False
#     driveLeft.value = 1.0
#     driveRight.value = 1.0
#
#
# def forwardTurnLeft():
#     forwardLeft.value = False
#     reverseLeft.value = True
#     forwardRight.value = False
#     reverseRight.value = True
#     driveLeft.value = 0.2
#     driveRight.value = 0.8
#
#
# def forwardTurnRight():
#     forwardLeft.value = False
#     reverseLeft.value = True
#     forwardRight.value = False
#     reverseRight.value = True
#     driveLeft.value = 0.8
#     driveRight.value = 0.2
#
#
# def main():
#     print("Starting")
#     allStop()
#     forwardDrive()
#     print("Step")
#     sleep(30)
#     # reverseDrive()
#     # print("Step")
#     # sleep(2)
#     # spinLeft()
#     # print("Step")
#     # sleep(2)
#     # SpinRight()
#     # print("Step")
#     # sleep(2)
#     # forwardTurnLeft()
#     # print("Step")
#     # sleep(2)
#     # forwardTurnRight()
#     # print("Step")
#     # sleep(2)
#
#     allStop()
#
#
# if __name__ == "__main__":
#     """ This is executed when run from the command line """
#     main()
