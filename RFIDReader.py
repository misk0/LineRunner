import RPi.GPIO as GPIO
import time
import SimpleMFRC522
import config


class RFIDReader:
    def __init__(self):
        self._running = True
        self._reader = SimpleMFRC522.SimpleMFRC522()

    def terminate(self):
        self._running = False

    def identify_obstacle(self, rfid_id):
        # shift last 4 digits in inverse order
        match = rfid_id[:4:-1]
        if not config.inside_obstacle:
            if match in config.obstacle_start:
                config.obstacle_number = config.obstacle_start.index(match)
                config.inside_obstacle = True
        else:
            for quad in config.obstacle_end:
                if match in quad:
                    config.obstacle_number = config.obstacle_end.index(quad)
                    config.inside_obstacle = False

    def run(self):
        try:
            while self._running:
                rfid_id = self._reader.read_id_no_block()
                if rfid_id is not None:
                    print(rfid_id)
                    self.identify_obstacle(rfid_id)
                    #time.sleep(0.2)
        finally:
            GPIO.cleanup()
