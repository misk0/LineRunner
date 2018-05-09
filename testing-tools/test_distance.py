import RPi.GPIO as GPIO  # Import the GPIO library.
import time  # Import time library

GPIO.setmode(GPIO.BOARD)

TRIG = 40  # GPIO4 = pin7
ECHO = 31  # GPIO14 = pin8

print
"Distance Measurement In Progress"

GPIO.setup(TRIG, GPIO.OUT)  # Set GPIO 4 TRIG pin 16 to output mode.
GPIO.setup(ECHO, GPIO.IN)  # Set GPIO 14 ECHO pin 18 to input mode.

GPIO.output(TRIG, False)
print
"Waiting For Sensor To Settle"
time.sleep(2)

i = 0

while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150

    distance = round(distance, 2)

    if distance > 2 and distance < 400:  # Check whether the distance is within range
        print("Distance:", distance, "cm")  # Print distance with 0.5 cm calibration
    else:
        print("Out Of Range")

    i = i + 1
    time.sleep(0.5)

GPIO.cleanup()
