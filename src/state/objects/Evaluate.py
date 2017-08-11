import sys
import os
import numpy as np
sys.path.append(os.path.dirname(__file__) + "/../../")

from state import state
from state.stateEnum import StateEnum
from helpers import configHelper
from helpers import processorHelper
from Navigation import Navigation

class Evaluate(Navigation):
    _current_word = 0        # Index para saber que palabra estoy evaluando
    _current_letter = 0      # Index para saber letra de la palabra que estoy evaluando
    _PREVIOUS_STATE = StateEnum.EVALUATE_MENU
    POINTS = 6
    LETTERS = 3

    def __init__(self, level_number):
        super(Evaluate, self).__init__()
        self.number = level_number
        self.words = configHelper.get_level_config('evaluation', self.number)['words']
        self.output = processorHelper.get_output_processor()
        self._print_welcome_message()
        self._initialize_matrix()

    def _print_welcome_message(self):
        print("Nivel " + str(self.number) + " de evaluacion")
        self._print_current_word()

    def _set_attributes(self):
        super(Evaluate, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE

    def _initialize_matrix(self):
       self.braille_matrix = np.zeros((self.LETTERS, self.POINTS), dtype=np.int)

    def process_input(self, input_value):
        if input_value in range(1, self.POINTS + 1):
            self._fill_braille_matrix(input_value)

        return super(Evaluate, self).process_input(input_value)

    def _move_right(self):
        self._current_letter += 1
        self._verify_overflow()

    def _move_left(self):
        self._current_letter -= 1
        self._verify_overflow()

    def _select_option(self):
        evaluation_result = self._evaluate()
        
        if evaluation_result:
            if not self._is_last_word():
                print("Palabra escrita correctamente. Se pasa a la siguiente palabra")
                self._go_to_next_word()
            else:
                self._back_to_menu()
        else:
            print("Palabra escrita de forma erronea.")

    def _go_to_next_word(self):
        self._current_word += 1
        self._reset_matrix()
        self._print_current_word()

    def _reset_matrix(self):
        self._initialize_matrix()
        self._current_letter = 0
    
    def _verify_overflow(self):
        if self._current_letter < 0:
            self._current_letter = 0
        elif self._current_letter == len(self.words[self._current_word]):
            self._current_letter -= 1

    def _fill_braille_matrix(self, input_value):
        point = input_value - 1
        
        if self.braille_matrix[self._current_letter][point] == 0:
            self.braille_matrix[self._current_letter][point] = 1
        else:
            self.braille_matrix[self._current_letter][point] = 0

        self._write()

    def _write(self):
        symbols = self._transform_points_into_symbols()
        self.output.write(symbols)

    def _transform_points_into_symbols(self):
        symbols = ""
        for i in range(len(self.words[self._current_word])):
            braille_points = ""
            for j in range(self.POINTS):
                braille_points += str(self.braille_matrix[i][j])
            symbols += self._get_and_format_symbol(braille_points)
        return symbols

    def _evaluate(self):
        result = self._transform_points_into_symbols().lower()
        print("Palabra ingresada: " + result + " - Palabra correcta: " + self.words[self._current_word])
        return True  # Deberia devolver result == self.words[self._current_word]
        
    def _print_current_word(self):
        print(self.words[self._current_word])

    def _is_last_word(self):
        return self._current_word == (len(self.words) - 1)

    def _back_to_menu(self):
        print("Se termino el nivel " + str(self.number) + " de evaluacion. Volviendo al menu de evaluacion ...")
        state.set_state(self._previous_state.key)
    
    def _get_and_format_symbol(self, braille_points):
        symbol = configHelper.get_symbol(braille_points)
        return symbol.replace('\n', '').replace('\r', '')