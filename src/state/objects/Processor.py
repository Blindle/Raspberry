import helpers.musicHelper as musicHelper
from state import state

class Processor(object): 
    def __init__(self):
        self._set_attributes()

    def process_input(self, input_value):
        if input_value == "right":
            self._move_right()

        elif input_value == "left":
            self._move_left()

        elif input_value == "enter":
            self._select_option()

        elif input_value == "back":
            self._back_to_previous_state()
        
    def _move_right(self):
        pass
    
    def _move_left(self):
        pass

    def _select_option(self):
        pass
    
    def _back_to_previous_state(self):
        print("Regresando a " + self._previous_state.real_name)
        self._initialize_output()
        musicHelper.play_back_to_action(self._previous_state.key)
        state.set_state(self._previous_state.key)
    
    def _verify_overflow(self):
        pass

    def _set_attributes(self):
        self._previous_state = None
        self.output = None

    def _print_current_option(self):
        pass

    def _initialize_output(self):
        if not self.output is None:
            self.output.initialize()

    def _finished_level(self, current_state, level_number):
        print("Se termino el nivel {} de {}. Volviendo al {} ...".format(str(level_number), current_state.real_name, self._previous_state.real_name))
        self._initialize_output()
        musicHelper.play_end_of_module_action(current_state.key, level_number, self._previous_state.key)
        state.set_state(self._previous_state.key)