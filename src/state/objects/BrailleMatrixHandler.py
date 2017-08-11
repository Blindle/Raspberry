import sys
import os
import numpy as np
sys.path.append(os.path.dirname(__file__) + "/../../")

from helpers import configHelper
from helpers import processorHelper
from Navigation import Navigation

class BrailleMatrixHandler(Navigation):
    _current_letter = 0
    _POINTS_SIZE = 6

    def __init__(self):
        super(BrailleMatrixHandler, self).__init__()
        self.output = processorHelper.get_output_processor()
        self._initialize_matrix()
        self._print_welcome_message()

    def _set_attributes(self):
        super(BrailleMatrixHandler, self)._set_attributes()
        self._letters_size = 0

    def _initialize_matrix(self):
       self.braille_matrix = np.zeros((self._letters_size, self._POINTS_SIZE), dtype=np.int)

    def process_input(self, input_value):
        if input_value in range(1, self._POINTS_SIZE + 1):
            self._fill_braille_matrix(input_value)

        return super(BrailleMatrixHandler, self).process_input(input_value)

    def _move_right(self):
        self._current_letter += 1
        self._verify_overflow()

    def _move_left(self):
        self._current_letter -= 1
        self._verify_overflow()

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

    def _transform_points_into_symbols(self, rows_size):
        symbols = ""
        for i in range(rows_size):
            braille_points = ""
            for j in range(self._POINTS_SIZE):
                braille_points += str(self.braille_matrix[i][j])
            symbols += self._get_and_format_symbol(braille_points)
        return symbols

    def _get_and_format_symbol(self, braille_points):
        symbol = configHelper.get_symbol(braille_points)
        return symbol.replace('\n', '').replace('\r', '')