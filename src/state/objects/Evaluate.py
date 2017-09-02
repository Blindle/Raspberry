import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../../")

from state import state
from state.stateEnum import StateEnum
from helpers import configHelper
from helpers import processorHelper
from BrailleMatrixHandler import BrailleMatrixHandler

class Evaluate(BrailleMatrixHandler):
    _index_current_word = 0
    _PREVIOUS_STATE = StateEnum.EVALUATE_MENU
    _error_counter = 0

    def __init__(self, level_number):
        self.number = level_number
        self.words = configHelper.get_level_config('evaluation', self.number)['words']
        super(Evaluate, self).__init__()

    def _set_attributes(self):
        super(Evaluate, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE

    def _print_welcome_message(self):
        print("Nivel " + str(self.number) + " de evaluacion")
        print(self._get_current_word())

    def _select_option(self):
        evaluation_result = self._evaluate()
        
        if evaluation_result:
            if not self._is_last_word():
                print("Palabra escrita correctamente. Se pasa a la siguiente palabra")
                self._go_to_next_word()
                self._error_counter = 0
            else:
                self._back_to_menu()
        else:
            print("Palabra escrita de forma erronea.")
            self._error_counter += 1

    def _go_to_next_word(self):
        self._index_current_word += 1
        self._reset_matrix()
        print(self._get_current_word())

    def _back_to_menu(self):
        print("Se termino el nivel " + str(self.number) + " de evaluacion. Volviendo al menu de evaluacion ...")
        state.set_state(self._previous_state.key)

    def _reset_matrix(self):
        self._initialize_matrix()
        self._current_letters_size = self._LETTERS_SIZE
        self._current_letter = 0

    def _evaluate(self):
        result = self._transform_points_into_symbols(self._current_letters_size).lower()
        print("Palabra ingresada: " + result + " - Palabra correcta: " + self._get_current_word())
        return result == self._get_current_word() or self._error_counter == 2

    def _is_last_word(self):
        return self._index_current_word == (len(self.words) - 1)

    def _get_current_word(self):
        return self.words[self._index_current_word]