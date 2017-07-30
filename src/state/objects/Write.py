import sys
import os
import numpy as np
sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum
from helpers import processorHelper
from helpers import configHelper
from Navigation import Navigation

class Write(Navigation):
    _PREVIOUS_STATE = StateEnum.MENU
    POINT = 6
    letter, current_letter = 4, 0  #cambiar nombre de variable letter

    def __init__(self):
        super(Write, self).__init__()
        self.output = processorHelper.get_output_processor()
        self._initialize_matrix()
        self._print_welcome_message()

    def _set_attributes(self):
        super(Write, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE

    def process_input(self, input_value):
        if input_value in range(1, self.POINT + 1):
            self._fill_braille_matrix(input_value)

        return super(Write, self).process_input(input_value)
    
    def _move_right(self):
        self.current_letter += 1
        self._verify_overflow()

    def _move_left(self):
        self.current_letter -= 1
        self._verify_overflow()

    def _verify_overflow(self):
        if self.current_letter < 0:
            self.current_letter = 0

        elif self.current_letter == self.letter:
            self._resize_matrix()
    
    def _print_welcome_message(self):
        print("Comienza la escritura libre, toque boton Atras para salir ...")

    def _initialize_matrix(self):
       self.braille_matrix = np.zeros((self.letter, self.POINT), dtype=np.int)

    def _fill_braille_matrix(self, input_value):
        point = input_value - 1
        
        if self.braille_matrix[self.current_letter][point] == 0:
            self.braille_matrix[self.current_letter][point] = 1
        else:
            self.braille_matrix[self.current_letter][point] = 0

        self._write()

    def _write(self):
        symbols = self._transform_points_into_symbols()
        self.output.write(symbols)

    def _transform_points_into_symbols(self):
        symbols = ""
        for i in range(self.letter):
            braille_points = ""
            for j in range(self.POINT):
                braille_points += str(self.braille_matrix[i][j])
            symbols += configHelper.get_symbol(braille_points)
        return symbols

    def _resize_matrix(self):
        self.letter += 1
        self.braille_matrix.resize((self.letter, self.POINT))