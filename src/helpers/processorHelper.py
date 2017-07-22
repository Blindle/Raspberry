import configHelper
from input.console import ConsoleInput
from input.buttons import ButtonsInput
from output.console import ConsoleOutput
from output.arduino import ArduinoOutput

CONFIG = configHelper.get_config()

def get_input_processor():
    if CONFIG['input'] == 'console':
        my_input = ConsoleInput()
    else:
        my_input = ButtonsInput()
    return my_input

def get_output_processor():
    if CONFIG['output'] == 'console':
        my_output = ConsoleOutput()
    else:
        my_output = ArduinoOutput(9600)
    return my_output