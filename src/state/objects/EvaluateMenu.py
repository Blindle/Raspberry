import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state import state


class EvaluateMenu:

    MENU_OPTIONS = ["Nivel 1", "Nivel 2", "Nivel 3"]
    MENU_VALUES = [1, 2, 3]
    CURRENT_OPTION = 0

    def __init__(self):
        print(self.MENU_OPTIONS[self.CURRENT_OPTION])

    def process_input(self, input_value):

        if input_value == "right":
            self.CURRENT_OPTION += 1
            self._verify_overflow()
            print(self.MENU_OPTIONS[self.CURRENT_OPTION])

        if input_value == "left":
            self.CURRENT_OPTION -= 1
            self._verify_overflow()
            print(self.MENU_OPTIONS[self.CURRENT_OPTION])

        if input_value == "enter":
            print("Entrando a " +
                  self.MENU_OPTIONS[self.CURRENT_OPTION] + " ...")
            state.set_state('evaluate', self.MENU_VALUES[self.CURRENT_OPTION])

        if input_value == "back":
            print("Regresando a menu principal")
            state.set_state("menu")

    def _verify_overflow(self):
        if self.CURRENT_OPTION == len(self.MENU_OPTIONS):
            self.CURRENT_OPTION = 0
            return

        if self.CURRENT_OPTION == -1:
            self.CURRENT_OPTION = len(self.MENU_OPTIONS) - 1