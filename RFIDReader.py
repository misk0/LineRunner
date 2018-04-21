import RPi.GPIO as GPIO
import time

import SimpleMFRC522


class RFIDReader:
    def __init__(self):
        self._running = True
        self._reader = SimpleMFRC522.SimpleMFRC522()

    def terminate(self):
        self._running = False

    def run(self):
        try:
            while self._running:
                rfid_id = self._reader.read_id_no_block()
                if rfid_id is not None:
                    print(rfid_id)
                    time.sleep(0.2)
        finally:
            GPIO.cleanup()
