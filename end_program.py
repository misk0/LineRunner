from RPi import GPIO
import signal
import sys
import config
import RFIDReader


def end_read(signal,frame):
    print("\nCtrl+C captured, ending read.")
    config.drive_left.stop()
    config.drive_right.stop()
    # config.servo_pwm.stop()
    # rfid.terminate()
    GPIO.cleanup()
    sys.exit()