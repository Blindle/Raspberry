import sys
import os
import helpers.musicHelper as musicHelper
sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum
from Menu import Menu
from state import state

class EvaluateMenu(Menu):
    _STATE_OPTIONS = [StateEnum.LEVEL_1, StateEnum.LEVEL_2, StateEnum.LEVEL_3]
    _PREVIOUS_STATE = StateEnum.MENU
    _NEXT_STATE = StateEnum.EVALUATE

    def __init__(self):
        super(EvaluateMenu, self).__init__()

    def _set_attributes(self):
        super(EvaluateMenu, self)._set_attributes()
        self.state_options = self._STATE_OPTIONS
        self._previous_state = self._PREVIOUS_STATE
        self._next_state = self._NEXT_STATE

    def _play_enter_action(self):
        navigation_sound = self._NEXT_STATE.key + '-level' + str(self.state_options[self.current_option].key)
        musicHelper.play_enter_action(navigation_sound)