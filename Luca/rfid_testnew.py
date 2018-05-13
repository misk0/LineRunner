#!/usr/bin/env python
import RPi.GPIO as GPIO
import signal
import time
import sys
import config

from pirc522 import RFID


GPIO.setmode(GPIO.BOARD)

GPIO.setup(config.right_motor_pwm, GPIO.OUT)
GPIO.setup(config.right_motor_direction, GPIO.OUT)
GPIO.setup(config.right_motor_direction_inv, GPIO.OUT)
GPIO.setup(config.left_motor_direction, GPIO.OUT)
GPIO.setup(config.left_motor_direction_inv, GPIO.OUT)
GPIO.setup(config.left_motor_pwm, GPIO.OUT)


pwm1 = GPIO.PWM(config.right_motor_pwm, 500)  # Initialize PWM on pwmPin 100Hz frequency
pwm2 = GPIO.PWM(config.left_motor_pwm, 500)  # Initialize PWM on pwmPin 100Hz frequency

pwm1.start(0)  # Start PWM with 0% duty cycle
pwm2.start(0)  # Start PWM with 0% duty cycle

GPIO.output(config.right_motor_direction, True)
GPIO.output(config.right_motor_direction_inv, False)
GPIO.output(config.left_motor_direction, True)
GPIO.output(config.left_motor_direction_inv, False)

I = 0

pwm1.ChangeDutyCycle(100)
pwm2.ChangeDutyCycle(100)


run = True
rdr = RFID()
util = rdr.util()
util.debug = True

def end_read(signal,frame):
    global run
    print("\nCtrl+C captured, ending read.")
    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)
    pwm1.stop()
    pwm2.stop()
    # rfid.terminate()
    # GPIO.cleanup()
    run = False
    # rdr.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, end_read)

print("Starting")



while run:
    rdr.wait_for_tag()
    # print("no")
    (error, data) = rdr.request()
    if not error:
        print("\nDetected: " + format(data, "02x"))

    (error, uid) = rdr.anticoll()
    if not error:
        esa0 = hex(uid[0])
        esa1 = hex(uid[1])
        esa2 = hex(uid[2])
        esa3 = hex(uid[3])
        # esa = esa[2:10]
        print(esa0,esa1,esa2,esa3)
        # print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))


        # print("Setting tag")
        # util.set_tag(uid)
        # print("\nAuthorizing")
        # #util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
        # util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
        # print("\nReading")
        # util.read_out(4)
        # print("\nDeauthorizing")
        # util.deauth()

time.sleep(1)