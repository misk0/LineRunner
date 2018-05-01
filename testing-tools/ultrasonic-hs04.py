import RPi.GPIO as GPIO
import time
import config

GPIO.setmode(GPIO.BOARD)


def measure_distance(sensor_id):
    GPIO.output(config.ultrasonic_trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(config.ultrasonic_trigger_pin, False)

    complex_distance = 0
    retries = 0
    for i in range(3):
        while GPIO.input(sensor_id) == 0:
            pulse_start = time.time()

        while GPIO.input(sensor_id) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        if distance >= 0:
            retries += 1
            complex_distance += distance

    complex_distance = round(complex_distance / retries)
    return complex_distance


GPIO.setup(config.ultrasonic_trigger_pin, GPIO.OUT)
GPIO.setup(config.ultrasonic_pin1, GPIO.IN)
GPIO.setup(config.ultrasonic_pin2, GPIO.IN)
GPIO.setup(config.ultrasonic_pin3, GPIO.IN)


GPIO.output(config.ultrasonic_trigger_pin, False)
print("Waiting For Sensor To Settle")
time.sleep(1)

for i in range(10):
    print("Sensor 1 : ", measure_distance(config.ultrasonic_pin1))
    print("Sensor 2 : ", measure_distance(config.ultrasonic_pin2))
    print("Sensor 3 : ", measure_distance(config.ultrasonic_pin3))
    time.sleep(1)

GPIO.cleanup()
