import configHelper
from output.console import ConsoleOutput
from output.arduino import ArduinoOutput

CONFIG = configHelper.get_config()

def get_input_processor():
    if CONFIG['input'] == 'console':
        from input.console import ConsoleInput as Input
    else:
        from input.buttons import ButtonsInput as Input
    return Input()

def get_output_processor():
    if CONFIG['output'] == 'console':
        my_output = ConsoleOutput()
    else:
        my_output = ArduinoOutput(9600)
    return my_output