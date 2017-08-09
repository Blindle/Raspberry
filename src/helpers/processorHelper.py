import configHelper
from input_finder import Input
from output.console import ConsoleOutput
from output.arduino import ArduinoOutput

CONFIG = configHelper.get_config()

def get_input_processor():
    return Input()

def get_output_processor():
    if CONFIG['output'] == 'console':
        my_output = ConsoleOutput()
    else:
        my_output = ArduinoOutput(9600)
    return my_output

def _import_buttons_input_module():
    from input.buttons import ButtonsInput