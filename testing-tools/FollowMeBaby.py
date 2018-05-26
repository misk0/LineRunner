import RPi.GPIO as GPIO
import config
from time import sleep

config.init()

# pin = [config.line_follow_rmax, config.line_follow_lmax, config.line_follow_mid, config.line_follow_lmin, config.line_follow_rmin]
        # pin[0]: sensore esterno destra     //Nello schizzo S4
        # pin[4]: sensore interno destra     //Nello schizzo S2
        # pin[1]: sensore esterno sinistra   //Nello schizzo S5
        # pin[3]: sensore interno sinistra   //Nello schizzo S3
        # pin[2]: sensore centrale           //Nello schizzo S1
        # pin[5]: sensore centrale arretrato //Nello schizzo S6


def FollowMe():
    # i = 0
    # while i < 5:
    #     if GPIO.input(pin[i]) == 1:
    #         print("PIN {} black".format(i))
    #     i += 1

    # Curva dolce verso sinistra
    if (GPIO.input(config.line_follow_lmin) == 1 and GPIO.input(config.line_follow_mid) == 0) or (GPIO.input(config.line_follow_lmin) == 1 and GPIO.input(config.line_follow_mid) == 1):
        while GPIO.input(config.line_follow_mid) == 0:
            config.walk_speed_left = config.walk_speed_left - 0.05

    # Curva dolce verso destra
    if (GPIO.input(config.line_follow_rmin) == 1 and GPIO.input(config.line_follow_mid) == 0) or (GPIO.input(config.line_follow_rmin) == 1 and GPIO.input(config.line_follow_mid) == 1):
    # print("# v motore sinistro > v motore destro")
        print("dolcedestra")
        while GPIO.input(config.line_follow_mid) == 0:
             config.walk_speed_right = config.walk_speed_right - 0.05

     # Curva a 90° verso destra
     # -1*(v motore destro) = v motore sinistro
    if GPIO.input(config.line_follow_mid) == 0 and GPIO.input(config.line_follow_lmin) == 0 and GPIO.input(config.line_follow_rmin) == 0 and GPIO.input(config.line_follow_rmax) == 0 and GPIO.input(config.line_follow_lmax) == 1:
         print("90destra")
         while GPIO.input(config.line_follow_mid) == 0:
            # GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
            # GPIO.output(config.left_motor_direction, GPIO.HIGH)
            config.drive_right.ChangeDutyCycle(0)
            GPIO.output(config.right_motor_direction, GPIO.LOW)
            GPIO.output(config.right_motor_direction_inv, GPIO.HIGH)
            config.drive_right.ChangeDutyCycle(config.walk_speed_right)

                    # Curva a 90° verso sinistra
                    # -1*(v motore sinistro) = v motore destro
    if GPIO.input(config.line_follow_mid) == 0 and GPIO.input(config.line_follow_lmin) == 0 and GPIO.input(config.line_follow_rmin) == 0 and GPIO.input(config.line_follow_lmax) == 0 and GPIO.input(config.line_follow_rmax) == 1:
        while GPIO.input(config.line_follow_mid) == 0:
            config.drive_left.ChangeDutyCycle(0)
            GPIO.output(config.left_motor_direction, GPIO.LOW)
            GPIO.output(config.left_motor_direction_inv, GPIO.HIGH)
            config.drive_right.ChangeDutyCycle(config.walk_speed_left)
            # GPIO.output(config.right_motor_direction, GPIO.HIGH)
            # GPIO.output(config.right_motor_direction_inv, GPIO.LOW)

    # v motore destro = v motore sinistro
    if GPIO.input(config.line_follow_mid) == 1:  # Se legge nero
        print("nero")
        #    print("v motore destro = v motore sinistro")
        GPIO.output(config.left_motor_direction, GPIO.HIGH)
        GPIO.output(config.left_motor_direction_inv, GPIO.LOW)
        GPIO.output(config.right_motor_direction, GPIO.HIGH)
        GPIO.output(config.right_motor_direction_inv, GPIO.LOW)
        config.walk_speed_right = 58
        config.walk_speed_left = 60

