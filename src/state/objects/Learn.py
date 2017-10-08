import sys
import os
sys.path.append(os.path.dirname(__file__) + "/../../")

from state import state
from state.stateEnum import StateEnum
from helpers import configHelper
from helpers import processorHelper
from helpers import musicHelper
from Processor import Processor

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
            self._back_to_menu()
    
    def _move_left(self):
        self.current_word -= 1
        if not self._verify_overflow():
            self._print_word()
            self._play_word()
        else:
            self.current_word = 0

    # FIXME: Ver si este metodo se puede pasar a la clase Processor, ya que la clase Evaluate tiene el mismo
    def _back_to_menu(self):
        print("Se termino el nivel " + str(self.number) + " de aprendizaje. Volviendo al menu de aprendizaje ...")
        musicHelper.play_end_of_module_action(StateEnum.LEARN.key, self.number, self._previous_state.key)
        state.set_state(self._previous_state.key)

    def _verify_overflow(self):
        return self.current_word == -1 or self.current_word == len(self.words)

    def _play_word(self):
        musicHelper.play_navigation_sound("wordExplanation")
        musicHelper.play_word(self.words[self.current_word])
        if configHelper.get_config()['wordSpelling'] == "enabled":
            musicHelper.play_word_spell_out(self.words[self.current_word].upper())
    
    def _print_word(self):
        word = self.words[self.current_word]
        print(word)
        self.output.write(word.upper())

    def _print_welcome_message(self):
        print("Nivel " + str(self.number) + " de aprendizaje")