import sys
import os
import helpers.musicHelper as musicHelper

from state import state
from state.stateEnum import StateEnum
from Menu import Menu
from state import state

class ConfigurationMenu(Menu):
    _STATE_OPTIONS = [StateEnum.REGULATION]
    _PREVIOUS_STATE = StateEnum.MENU
    _NEXT_STATE = StateEnum.REGULATION

    def __init__(self):
        super(ConfigurationMenu, self).__init__()

    def _set_attributes(self):
        super(ConfigurationMenu, self)._set_attributes()
        self.state_options = self._STATE_OPTIONS
        self._previous_state = self._PREVIOUS_STATE
        self._next_state = self._NEXT_STATE

    def _play_enter_action(self):
        navigation_sound = self._NEXT_STATE.key
        musicHelper.play_enter_action(navigation_sound)