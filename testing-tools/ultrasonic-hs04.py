import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
ECHO2 = 5


def measure_distance(sensor_id):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO2) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO2) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance


GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(ECHO2, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

for i in range(10):
    rez1 = measure_distance(1)
    time.sleep(0.1)
    rez2 = measure_distance(1)
    time.sleep(0.1)
    rez3 = measure_distance(1)
    final = round((rez1 + rez2 + rez3) / 3, 2)

    print("Distance : ", final)
    time.sleep(0.7)

GPIO.cleanup()
