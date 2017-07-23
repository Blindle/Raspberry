import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum
from helpers import processorHelper
from helpers import configHelper

class Write:

    POINT, LETTER = 6, 4
    current_letter = 0

    def __init__(self):
        print("Comienza la escritura libre, toque boton Atras para salir ...")
        self.output = processorHelper.get_output_processor()
        self._initialize_matrix()

    def process_input(self, input_value):
        if input_value in range(1, self.POINT + 1):
            point = input_value - 1
            
            if self.word[self.current_letter][point] == 0:
                self.word[self.current_letter][point] = 1
            else:
                self.word[self.current_letter][point] = 0
            self._write()

        elif input_value == "right":
            self.current_letter += 1

        elif input_value == "left":
            self.current_letter -= 1

        elif input_value == "back":
            print("Regresando a " + StateEnum.MENU.realName)
            state.set_state(StateEnum.MENU.key)

    def _verify_overflow(self):
        pass

    def _initialize_matrix(self):
       self.word = [[0 for x in range(self.POINT)] for y in range(self.LETTER)]

    def _write(self):
        words = ["" for x in range(self.LETTER)]
        for i in range(self.LETTER):
            letter = ""
            for j in range(self.POINT):
                letter += str(self.word[i][j])
            words[i] = configHelper.get_symbol(letter)
        self.output.write_words(words)