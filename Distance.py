import RPi.GPIO as GPIO
import time
import config


def measure_distance(sensor_pos, debug=False):
    complex_distance = 0
    retries = 0
    pulse_start = 0
    pulse_end = 0
    for counter in range(15):
        GPIO.output(config.ultrasonic_triggers[sensor_pos], GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(config.ultrasonic_triggers[sensor_pos], GPIO.LOW)
        while GPIO.input(config.ultrasonic_pins[sensor_pos]) == 0:
            pulse_start = time.time()

        while GPIO.input(config.ultrasonic_pins[sensor_pos]) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        if debug:
            print("Sensor : %s Current distance: %s" % (sensor_pos, distance))
        if complex_distance == 0:
            complex_distance = distance

        if distance < complex_distance:
            complex_distance = distance
        time.sleep(0.05)

    return complex_distance



