import sys
import os
import helpers.musicHelper as musicHelper
sys.path.append(os.path.dirname(__file__) + "../")

from state.stateEnum import StateEnum
from Menu import Menu
from state import state

class MainMenu(Menu):
    _STATE_OPTIONS = [StateEnum.LEARN_MENU, StateEnum.WRITE, StateEnum.EVALUATE_MENU, StateEnum.CONFIG]

    def __init__(self):
        super(MainMenu, self).__init__()
    
    def _back_to_previous_state(self):
        pass

    def _set_attributes(self):
        super(MainMenu, self)._set_attributes()
        self.state_options = self._STATE_OPTIONS

    def _play_enter_action(self):
        musicHelper.play_enter_action(self.state_options[self.current_option].key)