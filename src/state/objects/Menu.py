import sys
import os
import helpers.musicHelper as musicHelper
sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum
from Navigation import Navigation

class Menu(Navigation):
    current_option = 0

    def __init__(self):
        super(Menu, self).__init__()
        self._print_current_option()

    def _set_attributes(self):
        super(Menu, self)._set_attributes()
        self.state_options = []
        self._next_state = ""

    def _move_right(self):
        self.current_option += 1
        self._verify_overflow()
        self._print_current_option()

    def _move_left(self):
        self.current_option -= 1
        self._verify_overflow()
        self._print_current_option()

    def _select_option(self):
        print("Entrando a " + self.state_options[self.current_option].real_name + " ...")
        self._play_enter_action()
        self._set_new_state()

    def _verify_overflow(self):
        if self.current_option == len(self.state_options):
            self.current_option = 0
            return

        if self.current_option == -1:
            self.current_option = len(self.state_options) - 1
    
    def _print_current_option(self):
        print(self.state_options[self.current_option].real_name)
        musicHelper.play_menu_option(self.state_options[self.current_option].key)

    # FIXME: Hacer que el metodo lo implementen las clases hijas, como _play_enter_action
    def _set_new_state(self):
        if self._next_state != "":
            state.set_state(self._next_state.key, self.state_options[self.current_option].key)
        else:
            state.set_state(self.state_options[self.current_option].key)

    def _play_enter_action(self):
        pass