import time
import cv2
import RPi.GPIO as GPIO
from opencv import picam
from opencv import config
from opencv import face


class Box(object):
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(config.BUTTON_PIN, GPIO.IN)
        GPIO.setup(config.LOCK_SERVO_PIN, GPIO.OUT)
        GPIO.setup(config.LOCKED_LED, GPIO.OUT)
        GPIO.setup(config.TESTING_LED, GPIO.OUT)
        GPIO.setup(config.UNLOCKED_LED, GPIO.OUT)
        self.servo = GPIO.PWM(config.LOCK_SERVO_PIN, 50)
        self.servo.start(0)
        self.servo.ChangeDutyCycle(0)
        self.button_state = GPIO.input(config.BUTTON_PIN)
        self.is_locked = None

    def lock(self):
        self.servo.ChangeDutyCycle(config.LOCK_SERVO_LOCKED)
        self.is_locked = True
        GPIO.output(config.LOCKED_LED, True)
        GPIO.output(config.TESTING_LED, False)
        GPIO.output(config.UNLOCKED_LED, False)

    def unlock(self):
        self.servo.ChangeDutyCycle(config.LOCK_SERVO_UNLOCKED)
        self.is_locked = False
        GPIO.output(config.LOCKED_LED, False)
        GPIO.output(config.TESTING_LED, False)
        GPIO.output(config.UNLOCKED_LED, True)

    def starttest(self):
        GPIO.output(config.TESTING_LED, True)

    def endtest(self):
        GPIO.output(config.TESTING_LED, False)

    def is_button_up(self):
        old_state = self.button_state
        self.button_state = GPIO.input(config.BUTTON_PIN)
        if old_state == config.BUTTON_DOWN and self.button_state == config.BUTTON_UP:
            time.sleep(20.0 / 1000.0)
            self.button_state = GPIO.input(config.BUTTON_PIN)
            if self.button_state == config.BUTTON_UP:
                return True
        return False