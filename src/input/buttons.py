import RPi.GPIO as GPIO
import time

class ButtonsInput:

    _buttons_pins = [21, 20, 16, 26, 19, 13]
    
    _MOVE_RIGHT = "right"
    _MOVE_LEFT = "left"
    _ENTER = "enter"
    _BACK = "back"
    _POINT_1 = 1
    _POINT_2 = 2

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
                
                if self._previous_buttons_state[index] == self._BUTTON_PRESSED and curr_state == self._BUTTON_NOT_PRESSED: # El boton se deja de presionar
                    self._previous_buttons_state[index] = curr_state

                elif self._previous_buttons_state[index] == self._BUTTON_NOT_PRESSED and curr_state == self._BUTTON_PRESSED: # Se presiona un boton
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

        GPIO.setup(self.btn_1, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.btn_2, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.btn_3, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.btn_4, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.btn_5, GPIO.IN, GPIO.PUD_UP)
        GPIO.setup(self.btn_6, GPIO.IN, GPIO.PUD_UP)
    
    def _init_previous_buttons_state_array(self):
        self._previous_buttons_state = []
        for i in range(0, len(self._buttons_pins)):
            self._previous_buttons_state.append(self._BUTTON_NOT_PRESSED)

    def _get_pin_value(self, pin):
        return {
            21: self._MOVE_RIGHT,
            20: self._MOVE_LEFT,
            16: self._ENTER,
            26: self._BACK,
            19: self._POINT_1,
            13: self._POINT_2
        }[pin]
