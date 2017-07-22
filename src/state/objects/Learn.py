import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../../")

from state import state
from state.stateEnum import StateEnum
from helpers import configHelper
from helpers import loadingHelper

class Learn:

    current_word = 0

    def __init__(self, level_number):
        self.number = level_number
        self.words = configHelper.get_level_config('learn', self.number)['words']
        self.output = loadingHelper.get_output_processer();
        print("Nivel " + str(self.number) + " de aprendizaje")
        print(self.words[self.current_word])

    def process_input(self, input_value):

        if input_value == "right":
            self.current_word += 1
            self._verify_overflow()
            word = self.words[self.current_word]
            print(word)
            self.output.write(word.upper())

        if input_value == "left":
            self.current_word -= 1
            self._verify_overflow()
            word = self.words[self.current_word]
            print(word)
            self.output.write(word.upper())

        if input_value == "back":
            print("Regresando a " + StateEnum.MENU.realName)
            state.set_state(StateEnum.MENU.key)

    def _verify_overflow(self):
        pass