import wiringpi
import time

# Motor speeds for this library are specified as numbers
# between -MAX_SPEED and MAX_SPEED, inclusive.
_max_speed = 480  # 19.2 MHz / 2 / 480 = 20 kHz
MAX_SPEED = 480

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(13, wiringpi.GPIO.PWM_OUTPUT) #pin33 GPIO13

wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetRange(480)
wiringpi.pwmSetClock(2)

wiringpi.digitalWrite(13, 0)
wiringpi.pwmWrite(13, 480)

time.sleep(10)

wiringpi.digitalWrite(13, 0)
wiringpi.pwmWrite(13, 0)



