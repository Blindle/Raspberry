import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state import state


class MainMenu:

    MENU_OPTIONS = ["Modo aprendizaje", "Modo escritura", "Modo evaluacion", "Configuracion"]
    MENU_VALUES = ["learn-menu", "write", "evaluate-menu", "config"]
    CURRENT_OPTION = 0

    def __init__(self):
        print(self.MENU_OPTIONS[self.CURRENT_OPTION])
        pass

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
            state.set_state(self.MENU_VALUES[self.CURRENT_OPTION])

    def _verify_overflow(self):
        if self.CURRENT_OPTION == len(self.MENU_OPTIONS):
            self.CURRENT_OPTION = 0
            return

        if self.CURRENT_OPTION == -1:
            self.CURRENT_OPTION = len(self.MENU_OPTIONS) - 1
