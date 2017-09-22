import helpers.musicHelper as musicHelper
import helpers.configHelper as configHelper

from Navigation import Navigation
from state.stateEnum import StateEnum

class WordSourceSelector(Navigation):
    _PREVIOUS_STATE = StateEnum.CONFIG
    _DEFAULT_SOURCE = "default"
    _CUSTOM_SOURCE = "custom"
    _SOURCES = [_DEFAULT_SOURCE, _CUSTOM_SOURCE]
    _current_option = 0

    def __init__(self):
        super(WordSourceSelector, self).__init__()
        self._play_source_word_sound("message")
        print("Fuente actual: " + self._current_config)
        self._play_source_word_sound(self._current_config)
        self._play_source_word_sound(self._get_current_option())
    
    def _set_attributes(self):
        super(WordSourceSelector, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE
        self._current_config = configHelper.get_config()['wordSource']

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
            self._current_option = len(self._SOURCES) - 1
        elif self._current_option == len(self._SOURCES):
            self._current_option = 0

    def _print_current_option(self):
        print("Fuente de datos " + self._get_current_option())
        self._play_source_word_sound(self._get_current_option())

    def _select_option(self):
        self._play_source_word_sound("selection")
        self._play_source_word_sound(self._get_current_option())
        configHelper.update_system_config("wordSource", self._get_current_option())
        self._generate_word_sounds()
        self._back_to_previous_state()

    def _get_current_option(self):
        return self._SOURCES[self._current_option]

    def _play_source_word_sound(self, name):
        musicHelper.play_navigation_sound("word-source-" + name)

    def _generate_word_sounds(self):
        level_words = []
        level_words.extend(configHelper.get_level_config("learn", 1)['words'])
        level_words.extend(configHelper.get_level_config("learn", 2)['words'])
        level_words.extend(configHelper.get_level_config("learn", 3)['words'])
        level_words.extend(configHelper.get_level_config("evaluation", 1)['words'])
        level_words.extend(configHelper.get_level_config("evaluation", 2)['words'])
        level_words.extend(configHelper.get_level_config("evaluation", 3)['words'])
        musicHelper.generate_word_sounds(level_words)