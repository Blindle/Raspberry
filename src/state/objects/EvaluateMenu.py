import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum
from Menu import Menu

class EvaluateMenu(Menu):
    def __init__(self):
        super(EvaluateMenu, self).__init__()
        self.state_options = [StateEnum.LEVEL_1, StateEnum.LEVEL_2, StateEnum.LEVEL_3]
        self._set_previous_state(StateEnum.MENU)
        self._print_current_option()

    def _select_option(self):
        print("Entrando a " +
                self.state_options[self.current_option].real_name + " ...")
        state.set_state(StateEnum.EVALUATE.key, self.state_options[self.current_option].key)