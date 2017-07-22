import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../../")

from state import state
from state.stateEnum import StateEnum
from helpers import configHelper
from helpers import processorHelper

class Learn:

    current_word = 0

    def __init__(self, level_number):
        self.number = level_number
        self.words = configHelper.get_level_config('learn', self.number)['words']
        self.output = processorHelper.get_output_processor()
        print("Nivel " + str(self.number) + " de aprendizaje")
        self._print_word()

    def process_input(self, input_value):

        if input_value == "right":
            self.current_word += 1
            if not self._verify_overflow():
                self._print_word()
            else:
                print("Se termino el nivel " + str(self.number) + " de aprendizaje. Saliendo al menu principal ...")
                state.set_state(StateEnum.MENU.key)

        if input_value == "left":
            self.current_word -= 1
            if not self._verify_overflow():
                self._print_word()
            else:
                self.current_word = 0

        if input_value == "back":
            print("Regresando a " + StateEnum.MENU.realName)
            state.set_state(StateEnum.MENU.key)

    def _verify_overflow(self):
        return self.current_word == -1 or self.current_word == len(self.words)
    
    def _print_word(self):
        word = self.words[self.current_word]
        print(word)
        self.output.write(word.upper())