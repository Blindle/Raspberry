import RPi.GPIO as GPIO
import time
from InputProcessor import InputProcessor

class ButtonsInput(InputProcessor):

    _buttons_pins = [17, 27, 22, 23, 24, 5, 6, 13, 19, 26]
    
    _MOVE_RIGHT = "right"
    _MOVE_LEFT = "left"
    _ENTER = "enter"
    _BACK = "back"
    _POINT_1 = 1
    _POINT_2 = 2
    _POINT_3 = 3
    _POINT_4 = 4
    _POINT_5 = 5
    _POINT_6 = 6

    _BUTTON_PRESSED = 0
    _BUTTON_NOT_PRESSED = 1

    sleep_time = 0.1

    def __init__(self):
    	self._configure_raspberry_pins()
        self._init_previous_buttons_state_array()

    def get_input(self):
        input_value = ""
    	while input_value == "":
            for index, pin in enumerate(self._buttons_pins):
                curr_state = GPIO.input(pin)
                
                if self._previous_buttons_state[index] == self._BUTTON_PRESSED and curr_state == self._BUTTON_NOT_PRESSED:
                    self._previous_buttons_state[index] = curr_state

                elif self._previous_buttons_state[index] == self._BUTTON_NOT_PRESSED and curr_state == self._BUTTON_PRESSED:
                    self._previous_buttons_state[index] = curr_state
                    input_value = self._get_pin_value(pin)
                    break
                
            time.sleep(self.sleep_time)
        return input_value

    def __del__(self):
    	pass

    def _configure_raspberry_pins(self):
        GPIO.setmode(GPIO.BCM) 
        GPIO.setwarnings(False)

        for pin in self._buttons_pins:
            GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    
    def _init_previous_buttons_state_array(self):
        self._previous_buttons_state = []
        for i in range(0, len(self._buttons_pins)):
            self._previous_buttons_state.append(self._BUTTON_NOT_PRESSED)

    def _get_pin_value(self, pin):
        return {
            17: self._MOVE_LEFT,
            27: self._POINT_1,
            22: self._POINT_2,
            23: self._POINT_3,
            24: self._BACK,
            5: self._ENTER,
            6: self._POINT_4,
            13: self._POINT_5,
            19: self._POINT_6,
            26: self._MOVE_RIGHT
        }[pin]
