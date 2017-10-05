# coding=utf-8

from helpers import processorHelper
from Processor import Processor
from state.stateEnum import StateEnum

import helpers.musicHelper as musicHelper

class EngineRegulation(Processor):
    _PREVIOUS_STATE = StateEnum.CONFIG
    _MOTORS_SIZE = 8
    _LEFT = "I"
    _RIGHT = "D"
    _CHAR_TO_SEND = "-" #FIXME: Cambiar por '¬'
    _LEFT_BUTTON_VALUE = 1
    _RIGHT_BUTTON_VALUE = 6
    _current_motor = 0
    
    def __init__(self):
        super(EngineRegulation, self).__init__()
        self.output = processorHelper.get_output_processor()
        musicHelper.play_navigation_sound("regulation-message")
        self._print_current_motor()

    def _set_attributes(self):
        super(EngineRegulation, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE

    def process_input(self, input_value):
        if input_value == self._RIGHT_BUTTON_VALUE or input_value == self._LEFT_BUTTON_VALUE:
            self._regulate_engine(input_value)

        return super(EngineRegulation, self).process_input(input_value)

    def _move_right(self):
        self._current_motor += 1
        self._verify_overflow()
        self._print_current_motor()

    def _move_left(self):
        self._current_motor -= 1
        self._verify_overflow()
        self._print_current_motor()

    def _verify_overflow(self):
        if self._current_motor < 0:
            self._current_motor = self._MOTORS_SIZE - 1
        elif self._current_motor == self._MOTORS_SIZE:
            self._current_motor = 0

    def _print_current_motor(self):
        motor_str = str(self._current_motor + 1)
        print("Motor " + motor_str)
        musicHelper.play_navigation_sound("motor" + motor_str)

    def _regulate_engine(self, input_value):
        direction = ""
        if input_value == self._RIGHT_BUTTON_VALUE:
            direction = self._RIGHT
        else:
            direction = self._LEFT
        motor_number = self._current_motor
        message_to_send = "{}{}{}".format(self._CHAR_TO_SEND, direction, str(motor_number))

        print("Enviando " + message_to_send)
        self.output.write(message_to_send)