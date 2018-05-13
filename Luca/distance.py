import RPi.GPIO as GPIO
import time
import signal

ultra_pin = [31,32,33]
ultra_trigger = [7, 5, 29]

ultra_left = 0
ultra_center = 1
ultra_right = 2

GPIO.setmode(GPIO.BOARD)

GPIO.setup(ultra_trigger[ultra_left], GPIO.OUT)
GPIO.setup(ultra_trigger[ultra_center], GPIO.OUT)
GPIO.setup(ultra_trigger[ultra_right], GPIO.OUT)

GPIO.setup(ultra_pin[ultra_left], GPIO.IN)
GPIO.setup(ultra_pin[ultra_center], GPIO.IN)
GPIO.setup(ultra_pin[ultra_right], GPIO.IN)

def end_read(signal,frame):
    print("\nCtrl+C captured, ending read.")
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)

def measure_distance(sensor_id):
    complex_distance = 0
    retries = 0
    pulse_start = 0
    pulse_end = 0
    for i in range(3):
        GPIO.output(ultra_trigger[sensor_id], True)
        time.sleep(0.00001)
        GPIO.output(ultra_trigger[sensor_id], False)

        while GPIO.input(ultra_pin[sensor_id]) == 0:
            pulse_start = time.time()

        while GPIO.input(ultra_pin[sensor_id]) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        # if distance >= 0:
        #     retries += 1
        #     complex_distance += distance

    # complex_distance = round(complex_distance / retries)
    return distance

while True:
    print("Sensor left : ", measure_distance(ultra_left))
    print("Sensor center : ", measure_distance(ultra_center))
    print("Sensor right : ", measure_distance(ultra_right))

    time.sleep(1)

GPIO.cleanup()

