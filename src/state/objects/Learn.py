import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../../")

from state import state
from state.stateEnum import StateEnum
from helpers import configHelper
from helpers import processorHelper
from helpers import musicHelper
from Navigation import Navigation

class Learn(Navigation):
    current_word = 0

    def __init__(self, level_number):
        self.number = level_number
        self.words = configHelper.get_level_config('learn', self.number)['words']
        self.output = processorHelper.get_output_processor()
        print("Nivel " + str(self.number) + " de aprendizaje")
        self._print_word()

    def _move_right(self):
        self.current_word += 1
        if not self._verify_overflow():
            self._print_word()
            #musicHelper.play_word(self.words[self.current_word])
        else:
            print("Se termino el nivel " + str(self.number) + " de aprendizaje. Saliendo al menu ...")
            state.set_state(StateEnum.LEARN_MENU.key)
    
    def _move_left(self):
        self.current_word -= 1
        if not self._verify_overflow():
            self._print_word()
        else:
            self.current_word = 0

    def _back_to_previous_state(self):
        print("Regresando a " + StateEnum.LEARN_MENU.real_name)
        state.set_state(StateEnum.LEARN_MENU.key)

    def _verify_overflow(self):
        return self.current_word == -1 or self.current_word == len(self.words)
    
    def _print_word(self):
        word = self.words[self.current_word]
        print(word)
        self.output.write(word.upper())