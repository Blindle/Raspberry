import sys
import os
import helpers.musicHelper as musicHelper

from state import state
from state.stateEnum import StateEnum
from Menu import Menu
from state import state

class ConfigurationMenu(Menu):
    _STATE_OPTIONS = [StateEnum.REGULATION, StateEnum.WORDS_IMPORTER, StateEnum.WORD_SOURCE, StateEnum.SOUNDS_GENERATOR, StateEnum.WORD_SPELLING]
    _PREVIOUS_STATE = StateEnum.MENU

    def __init__(self):
        super(ConfigurationMenu, self).__init__()

    def _set_attributes(self):
        super(ConfigurationMenu, self)._set_attributes()
        self.state_options = self._STATE_OPTIONS
        self._previous_state = self._PREVIOUS_STATE

    def _play_enter_action(self):
        navigation_sound = self._get_current_option().key
        musicHelper.play_enter_action(navigation_sound)

    def _get_current_option(self):
        return self.state_options[self.current_option]

    def _set_new_state(self):
        state.set_state(self._get_current_option().key)