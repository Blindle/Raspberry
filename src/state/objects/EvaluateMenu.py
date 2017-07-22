import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum

class EvaluateMenu:

    MENU_OPTIONS = [StateEnum.LEVEL_1, StateEnum.LEVEL_2, StateEnum.LEVEL_3]
    CURRENT_OPTION = 0

    def __init__(self):
        print(self.MENU_OPTIONS[self.CURRENT_OPTION].realName)

    def process_input(self, input_value):

        if input_value == "right":
            self.CURRENT_OPTION += 1
            self._verify_overflow()
            print(self.MENU_OPTIONS[self.CURRENT_OPTION].realName)

        elif input_value == "left":
            self.CURRENT_OPTION -= 1
            self._verify_overflow()
            print(self.MENU_OPTIONS[self.CURRENT_OPTION].realName)

        elif input_value == "enter":
            print("Entrando a " +
                  self.MENU_OPTIONS[self.CURRENT_OPTION].realName + " ...")
            state.set_state(StateEnum.EVALUATE.key, self.MENU_OPTIONS[self.CURRENT_OPTION].key)

        elif input_value == "back":
            print("Regresando a " + StateEnum.EVALUATE_MENU.realName)
            state.set_state(StateEnum.EVALUATE_MENU.key)

    def _verify_overflow(self):
        if self.CURRENT_OPTION == len(self.MENU_OPTIONS):
            self.CURRENT_OPTION = 0
            return

        if self.CURRENT_OPTION == -1:
            self.CURRENT_OPTION = len(self.MENU_OPTIONS) - 1