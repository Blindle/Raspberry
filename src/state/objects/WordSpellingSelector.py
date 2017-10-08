import helpers.musicHelper as musicHelper
import helpers.configHelper as configHelper

from Processor import Processor
from state.stateEnum import StateEnum

class WordSpellingSelector(Processor):
    _PREVIOUS_STATE = StateEnum.CONFIG
    _ENABLED = "enabled"
    _DISABLED = "disabled"
    _OPTIONS = [_ENABLED, _DISABLED]
    _current_option = 0

    def __init__(self):
        super(WordSpellingSelector, self).__init__()
        self._play_source_word_spelling("message")
        print("Opcion actual: " + self._current_config)
        self._play_source_word_spelling(self._current_config)
        self._play_source_word_spelling("options")
        self._print_current_option()
    
    def _set_attributes(self):
        super(WordSpellingSelector, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE
        self._current_config = configHelper.get_config()['wordSpelling']

    def _move_right(self):
        self._current_option += 1
        self._verify_overflow()
        self._print_current_option()

    def _move_left(self):
        self._current_option -= 1
        self._verify_overflow()
        self._print_current_option()

    def _verify_overflow(self):
        if self._current_option < 0:
            self._current_option = len(self._OPTIONS) - 1
        elif self._current_option == len(self._OPTIONS):
            self._current_option = 0

    def _print_current_option(self):
        print("Opcion " + self._get_current_option())
        self._play_source_word_spelling(self._get_current_option())

    def _select_option(self):
        print "Ha seleccionado la opcion " + self._get_current_option() 
        self._play_source_word_spelling("selection")
        self._play_source_word_spelling(self._get_current_option())
        configHelper.update_system_config("wordSpelling", self._get_current_option())
        self._back_to_previous_state()

    def _get_current_option(self):
        return self._OPTIONS[self._current_option]

    def _play_source_word_spelling(self, name):
        musicHelper.play_navigation_sound("word-spelling-" + name)