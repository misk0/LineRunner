import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()
try:
    while True:
        rfid_id = reader.read_id_no_block()
        if rfid_id is not None:
            print(rfid_id)
        else:
            print("no")

            #time.sleep(0.2)
finally:
    GPIO.cleanup()
