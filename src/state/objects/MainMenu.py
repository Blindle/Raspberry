import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state.stateEnum import StateEnum
from Menu import Menu
from state import state

class MainMenu(Menu):
    _STATE_OPTIONS = [StateEnum.LEARN_MENU, StateEnum.WRITE, StateEnum.EVALUATE_MENU, StateEnum.CONFIG]

    def __init__(self):
        super(MainMenu, self).__init__()
        self.state_options = self._STATE_OPTIONS
        self._print_current_option()
    
    def _back_to_previous_state(self):
        pass