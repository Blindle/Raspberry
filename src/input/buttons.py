import RPi.GPIO as GPIO
import time

class ButtonsInput:

    btn_1 = 21
    btn_2 = 20
    btn_3 = 16
    btn_4 = 26
    btn_5 = 19
    btn_6 = 13

    _MOVE_RIGHT = "right"
    _MOVE_LEFT = "left"
    _ENTER = "enter"
    _BACK = "back"
    _ENTER = "enter"
    _POINT_1 = 1
    _POINT_2 = 2

    sleep_time = 0.1

    def __init__(self):
    	self._configure_raspberry_pins()

    def get_input(self):
        input_value = ""
    	while input_value == "":
            if GPIO.input(self.btn_1) == False:
                input_value = self._MOVE_RIGHT

            elif GPIO.input(self.btn_2) == False: 
                input_value = self._MOVE_LEFT

            elif GPIO.input(self.btn_3) == False:
                input_value = self._ENTER
            
            elif GPIO.input(self.btn_4) == False:
                input_value = self._BACK
            
            elif GPIO.input(self.btn_5) == False: 
                input_value = self._POINT_1
            
            elif GPIO.input(self.btn_6) == False: 
                input_value = self._POINT_2
            
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
