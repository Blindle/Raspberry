import sys
import os
import numpy as np
sys.path.append(os.path.dirname(__file__) + "/../../")

from helpers import configHelper
from helpers import processorHelper
from helpers import musicHelper
from Processor import Processor

class BrailleMatrixHandler(Processor):
    _current_letter = 0
    _POINTS_SIZE = 6
    _LETTERS_SIZE = 1

    def __init__(self):
        super(BrailleMatrixHandler, self).__init__()
        self.output = processorHelper.get_output_processor()
        self._initialize_matrix()
        self._print_welcome_message()
        musicHelper.play_letter_number(self._current_letter + 1)

    def _set_attributes(self):
        super(BrailleMatrixHandler, self)._set_attributes()
        self._current_letters_size = self._LETTERS_SIZE

    def _initialize_matrix(self):
       self.braille_matrix = np.zeros((self._LETTERS_SIZE, self._POINTS_SIZE), dtype=np.int)

    def process_input(self, input_value):
        if input_value in range(1, self._POINTS_SIZE + 1):
            self._fill_braille_matrix(input_value)

        return super(BrailleMatrixHandler, self).process_input(input_value)

    def _move_right(self):
        self._current_letter += 1
        self._verify_overflow()
        musicHelper.play_letter_number(self._current_letter + 1)
        if self._should_write_on_movement(self._current_letter, self._current_letter - 1):
            self._write()

    def _move_left(self):
        self._current_letter -= 1
        if self._current_letter >= 0:
            musicHelper.play_letter_number(self._current_letter + 1)
        self._verify_overflow()
        if self._should_write_on_movement(self._current_letter, self._current_letter + 1):
            self._write()

    def _verify_overflow(self):
        if self._current_letter < 0:
            self._current_letter = 0

        elif self._current_letter == self._current_letters_size:
            self._resize_matrix()

    def _resize_matrix(self):
        letters = configHelper.get_number_of_letters()
        if self._current_letters_size % letters == 0:
            self._current_letters_size += letters
        else:
            self._current_letters_size += 1
        self.braille_matrix.resize((self._current_letters_size, self._POINTS_SIZE))

    def _fill_braille_matrix(self, input_value):
        point = input_value - 1
        
        if self.braille_matrix[self._current_letter][point] == 0:
            self.braille_matrix[self._current_letter][point] = 1
        else:
            self.braille_matrix[self._current_letter][point] = 0

        self._write()

    def _write(self):
        symbols = self._transform_points_into_symbols(self._current_letters_size)
        output = self._get_output(symbols)
        self.output.write(output)

    def _get_output(self, symbols):
        number_of_letters = configHelper.get_number_of_letters()
        start = self._current_letter - (self._current_letter % number_of_letters)
        finish = start + number_of_letters
        return symbols[start:finish]

    def _transform_points_into_symbols(self, rows_size):
        symbols = ""
        for i in range(rows_size):
            braille_points = ""
            for j in range(self._POINTS_SIZE):
                braille_points += str(self.braille_matrix[i][j])
            symbols += self._get_and_format_symbol(braille_points)
        return symbols

    def _get_and_format_symbol(self, braille_points):
        return configHelper.get_symbol(braille_points)

    def _should_write_on_movement(self, current_letter, previous_letter):
        letters = configHelper.get_number_of_letters()
        if previous_letter < current_letter and previous_letter % letters == letters - 1:
            return True
        if (previous_letter > 1 and previous_letter % letters == 0 and
                previous_letter > current_letter):
            return True
        return False
