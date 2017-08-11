import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state.stateEnum import StateEnum
from helpers import processorHelper
from helpers import configHelper
from BrailleMatrixHandler import BrailleMatrixHandler

class Write(BrailleMatrixHandler):
    _PREVIOUS_STATE = StateEnum.MENU
    _LETTERS_SIZE = 4

    def __init__(self):
        super(Write, self).__init__()

    def _set_attributes(self):
        super(Write, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE
        self._letters_size = self._LETTERS_SIZE

    def _verify_overflow(self):
        if self._current_letter < 0:
            self._current_letter = 0

        elif self._current_letter == self._letters_size:
            self._resize_matrix()
    
    def _print_welcome_message(self):
        print("Comienza la escritura libre, toque boton Atras para salir ...")

    def _write(self):
        symbols = self._transform_points_into_symbols(self._letters_size)
        self.output.write(symbols)

    def _resize_matrix(self):
        self._letters_size += 1
        self.braille_matrix.resize((self._letters_size, self._POINTS_SIZE))