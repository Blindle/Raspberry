import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum
from Menu import Menu
from state import state

class LearnMenu(Menu):
    _STATE_OPTIONS = [StateEnum.LEVEL_1, StateEnum.LEVEL_2, StateEnum.LEVEL_3]
    _PREVIOUS_STATE = StateEnum.MENU
    _NEXT_STATE = StateEnum.LEARN

    def __init__(self):
        super(LearnMenu, self).__init__()
        self._previous_state = self._PREVIOUS_STATE
        self._next_state = self._NEXT_STATE
        self.state_options = self._STATE_OPTIONS
        self._print_current_option()