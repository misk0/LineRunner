import RPi.GPIO as GPIO  # Import the GPIO library.
import time  # Import time library
# from threading import Thread
# import RFIDReader
# import config

# config.init()

# Create thread for RFID reading
# rfid = RFIDReader.RFIDReader()
# rfidThread = Thread(target=rfid.run)
# rfidThread.start()

pwm1AvgSpeed = 60
pwm2AvgSpeed = 58

pwm1MinSpeed = 37
pwm2MinSpeed = 35

I = 0

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.

GPIO.setup(16, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(18, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(13, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(15, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(8, GPIO.OUT)  # Set GPIO pin 12 to output mode.
GPIO.setup(10, GPIO.OUT)  # Set GPIO pin 12 to output mode.

pwm1 = GPIO.PWM(16, 500)  # Initialize PWM on pwmPin 100Hz frequency
pwm2 = GPIO.PWM(18, 500)  # Initialize PWM on pwmPin 100Hz frequency

pwm1.start(0)  # Start PWM with 0% duty cycle
pwm2.start(0)  # Start PWM with 0% duty cycle

GPIO.output(13, False)
GPIO.output(8, True)
GPIO.output(15, False)
GPIO.output(10, True)

pwm1.ChangeDutyCycle(100)
pwm2.ChangeDutyCycle(100)

GPIO.output(13, True)
GPIO.output(8, False)
GPIO.output(15, True)
GPIO.output(10, False)

pwm1.ChangeDutyCycle(pwm1AvgSpeed)
pwm2.ChangeDutyCycle(pwm2AvgSpeed)

# while True:
#     dc = 1


lineSxMax = 33;
lineSxMin = 35;
lineMid = 36;
lineDxMin = 37;
lineDxMax = 38;

GPIO.setup(lineSxMax, GPIO.IN)
GPIO.setup(lineSxMin, GPIO.IN)
GPIO.setup(lineMid, GPIO.IN)
GPIO.setup(lineDxMin, GPIO.IN)
GPIO.setup(lineDxMax, GPIO.IN)

previousError = 0
Kp = 15
Kd = 15
Ki = 0
print("parto")
error = 0
while True:
    lineSxMaxValue = GPIO.input(lineSxMax)
    lineSxMinValue = GPIO.input(lineSxMin)
    lineMidValue = GPIO.input(lineMid)
    lineDxMinValue = GPIO.input(lineDxMin)
    lineDxMaxValue = GPIO.input(lineDxMax)
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 0 and lineDxMinValue == 0 and lineDxMaxValue == 1:
        error = 4
        # print("troppo sin")
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 0 and lineDxMinValue == 1 and lineDxMaxValue == 1:
        error = 3
        # print("quasitroppo sin")
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 0 and lineDxMinValue == 1 and lineDxMaxValue == 0:
        error = 2
        # print("unpopiu sin")
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 1 and lineDxMinValue == 1 and lineDxMaxValue == 0:
        error = 1
        # print("unpo sin")
    if lineSxMaxValue == 0 and lineSxMinValue == 0 and lineMidValue == 1 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        error = 0
        # print("mid")
    if lineSxMaxValue == 0 and lineSxMinValue == 1 and lineMidValue == 1 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        error = -1
        # print("unpo dx")
    if lineSxMaxValue == 0 and lineSxMinValue == 1 and lineMidValue == 0 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        error = -2
        # print("unpopiu dx")
    if lineSxMaxValue == 1 and lineSxMinValue == 1 and lineMidValue == 0 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        error = -3
        # print("quasitroppo sx")
    if lineSxMaxValue == 1 and lineSxMinValue == 0 and lineMidValue == 0 and lineDxMinValue == 0 and lineDxMaxValue == 0:
        error = -4
        # print("troppo dx")

    P = error
    I = I + error
    D = error-previousError
    PIDvalue = (Kp*P) + (Ki*I) + (Kd*D)

    if pwm1AvgSpeed-PIDvalue > 100:
        pwm1.ChangeDutyCycle(100)
    elif pwm1AvgSpeed - PIDvalue < pwm1MinSpeed:
        pwm1.ChangeDutyCycle(0)
    else:
        pwm1.ChangeDutyCycle(pwm1AvgSpeed - PIDvalue)

    if pwm2AvgSpeed + PIDvalue > 100:
        pwm2.ChangeDutyCycle(100)
    elif pwm2AvgSpeed + PIDvalue < pwm2MinSpeed:
        pwm2.ChangeDutyCycle(0)
    else:
        pwm2.ChangeDutyCycle(pwm2AvgSpeed + PIDvalue)


    previousError = error
    time.sleep(0.001)


pwm1.stop()
pwm2.stop()
# rfid.terminate()
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
