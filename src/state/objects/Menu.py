import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum
from Navigation import Navigation

class Menu(Navigation):
    current_option = 0
    previous_state = ""

    def __init__(self):
        super(Menu, self).__init__()

    def _move_right(self):
        self.current_option += 1
        self._verify_overflow()
        self._print_current_option()

    def _move_left(self):
        self.current_option -= 1
        self._verify_overflow()
        self._print_current_option()

    def _select_option(self):
        print("Entrando a " +
            self.state_options[self.current_option].real_name + " ...")
        self._set_new_state()

    def _back_to_previous_state(self):
        print("Regresando a " + self.previous_state.real_name)
        state.set_state(self.previous_state.key)

    def _verify_overflow(self):
        if self.current_option == len(self.state_options):
            self.current_option = 0
            return

        if self.current_option == -1:
            self.current_option = len(self.state_options) - 1
    
    def _print_current_option(self):
        print(self.state_options[self.current_option].real_name)

    def _set_state_options(self, options):
        self.state_options = options

    def _set_previous_state(self, prev_state):
        self.previous_state = prev_state

    def _set_new_state(self):
        pass