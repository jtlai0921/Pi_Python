import time

import cv2
import RPi.GPIO as GPIO

import picam
import config
import face


class Box(object):
    """Class to represent the state and encapsulate access to the hardware of 
    the treasure box."""
    def __init__(self):
        # Initialize lock servo and button.
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(config.BUTTON_PIN, GPIO.IN)
        GPIO.setup(config.LOCK_SERVO_PIN, GPIO.OUT)
        GPIO.setup(config.LOCKED_LED, GPIO.OUT)
        GPIO.setup(config.TESTING_LED, GPIO.OUT)
        GPIO.setup(config.UNLOCKED_LED, GPIO.OUT)
        self.servo = GPIO.PWM(config.LOCK_SERVO_PIN, 50)
        self.servo.start(0)
        self.servo.ChangeDutyCycle(0)
        # Set initial box state.
        self.button_state = GPIO.input(config.BUTTON_PIN)
        self.is_locked = None

    def lock(self):
        """Lock the box."""
        self.servo.ChangeDutyCycle(config.LOCK_SERVO_LOCKED)
        self.is_locked = True
        GPIO.output(config.LOCKED_LED, True)
        GPIO.output(config.TESTING_LED, False)
        GPIO.output(config.UNLOCKED_LED, False)

    def unlock(self):
        """Unlock the box."""
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
        """Return True when the box button has transitioned from down to up (i.e.
        the button was pressed)."""
        old_state = self.button_state
        self.button_state = GPIO.input(config.BUTTON_PIN)
        # Check if transition from down to up
        if old_state == config.BUTTON_DOWN and self.button_state == config.BUTTON_UP:
            # Wait 20 milliseconds and measure again to debounce switch.
            time.sleep(20.0/1000.0)
            self.button_state = GPIO.input(config.BUTTON_PIN)
            if self.button_state == config.BUTTON_UP:
                return True
        return False
