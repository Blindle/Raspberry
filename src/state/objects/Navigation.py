class Navigation(object): 
    def __init__(self):
        self.state_options = []

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
        pass
    
    def _set_state_options(self, options):
        pass
    
    def _verify_overflow(self):
        pass