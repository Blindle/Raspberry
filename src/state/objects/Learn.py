import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../../")

from state import state
from state.stateEnum import StateEnum
from helpers import configHelper

class Learn:
    def __init__(self, level_number):
        self.number = level_number
        self.words = configHelper.get_level_config('learn', self.number)['words']
        print("Nivel " + str(self.number) + " de aprendizaje")

    def process_input(self, input_value):

        if input_value == "back":
            print("Regresando a " + StateEnum.MENU.realName)
            state.set_state(StateEnum.MENU.key)

    def _verify_overflow(self):
        pass