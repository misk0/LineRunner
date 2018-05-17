import RPi.GPIO as GPIO
import time
import config


class FoundInSpace:
    def __init__(self):
        self._running = True
        self._pulse_start = 0
        self._pulse_end = 0
        GPIO.setup(config.ultrasonic_trigger_pin, GPIO.OUT)
        GPIO.setup(config.ultrasonic_pin1, GPIO.IN)
        GPIO.setup(config.ultrasonic_pin2, GPIO.IN)
        GPIO.setup(config.ultrasonic_pin3, GPIO.IN)
        GPIO.add_event_detect(config.ultrasonic_pin1, GPIO.BOTH, callback=self.get_the_signal)

    def get_the_signal(self, channel):
        self._pulse_start = time.time()
        if GPIO.input(config.ultrasonic_pin1) == 1:
            print("RISING time: ", self._pulse_start)
        else:
            print("FALLING time:", self._pulse_start)

    def terminate(self):
        self._running = False

    def measure_distance(self, sensor_id, debug=False):
        complex_distance = 0
        retries = 0
        pulse_start = 0
        pulse_end = 0


        for counter in range(3):
            self._pulse_start = 0
            self._pulse_end = 0
            GPIO.output(config.ultrasonic_trigger_pin, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(config.ultrasonic_trigger_pin, GPIO.LOW)
            #while GPIO.input(sensor_id) == 0:
            #GPIO.wait_for_edge(sensor_id, GPIO.RISING)

            pulse_start = time.time()

            while GPIO.input(sensor_id) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            print("Old time: ", pulse_duration)
            if self._pulse_start > 0 and self._pulse_end > 0:
                print("New time: ", self._pulse_end - self._pulse_start)

            distance = pulse_duration * 17150
            distance = round(distance, 2)

            print("Distance: ", distance)
            if debug:
                print("Sensor: %s Current distance: %s" % (sensor_id, distance))
            if 0 < distance < 400:
                retries += 1
                complex_distance += distance
            time.sleep(0.05)

        if retries > 0:
            complex_distance = round(complex_distance / retries, 2)
        return complex_distance

    def run(self):
        GPIO.output(config.ultrasonic_trigger_pin, False)
        print("Waiting For Sensor To Settle")
        time.sleep(1)

        while self._running:
            distance_left = self.measure_distance(config.ultrasonic_pin1, True)
            #distance_right = self.measure_distance(config.ultrasonic_pin2, True)
            print("Sensor LEFT : ", distance_left)
            #print("Sensor RIGHT : ", distance_right)

            # print("Sensor 3 : ", measure_distance(config.ultrasonic_pin3))
            time.sleep(1)
