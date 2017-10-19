import os
import sys

from helpers import configHelper, musicHelper, processorHelper
from Processor import Processor
from state import state
from state.stateEnum import StateEnum

sys.path.append(os.path.dirname(__file__) + "/../../")


class Learn(Processor):
    current_word = 0
    _PREVIOUS_STATE = StateEnum.LEARN_MENU

    def __init__(self, level_number):
        super(Learn, self).__init__()
        self.number = level_number
        self.words = configHelper.get_level_config('learn', self.number)['words']
        self.output = processorHelper.get_output_processor()
        self._print_welcome_message()
        self._print_word()
        self._play_word()

    def _set_attributes(self):
        super(Learn, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE

    def _move_right(self):
        self.current_word += 1
        if not self._verify_overflow():
            self._print_word()
            self._play_word()
        else:
            self._finished_level(StateEnum.LEARN, self.number)
    
    def _move_left(self):
        self.current_word -= 1
        if not self._verify_overflow():
            self._print_word()
            self._play_word()
        else:
            self.current_word = 0

    def _verify_overflow(self):
        return self.current_word == -1 or self.current_word == len(self.words)

    def _play_word(self):
        word = self._get_current_word()
        musicHelper.play_word(word)
        if configHelper.get_config()['wordSpelling'] == "enabled":
            musicHelper.play_word_spell_out(word.upper())
    
    def _print_word(self):
        word = self._get_current_word()
        print(word)
        self.output.write(word.upper())

    def _print_welcome_message(self):
        print("Nivel " + str(self.number) + " de aprendizaje")

    def _get_current_word(self):
        return self.words[self.current_word]