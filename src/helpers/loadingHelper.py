import sys
import os

sys.path.append(os.path.dirname(__file__) + "../")

import configHelper
from input.console import ConsoleInput
from input.buttons import ButtonsInput
from output.console import ConsoleOutput
from output.arduino import ArduinoOutput
from state import state

from state.objects.MainMenu import MainMenu

CONFIG = configHelper.get_config()

def get_input_processer():
    if CONFIG['input'] == 'console':
        my_input = ConsoleInput()
    else:
        my_input = ButtonsInput()
    return my_input

def get_output_processer():
    if CONFIG['output'] == 'console':
        my_output = ConsoleOutput()
    else:
        my_output = ArduinoOutput(9600)
    return my_output

def get_state_object():
    return {
        'menu': MainMenu(),
        'learn-menu': 'learn menu',
        'evaluate-menu': 'evaluate menu',
        'learn': 'learn',
        'write': 'write',
        'evaluate': 'evaluate',
        'config': 'config'
    }.get(state.get_state(), '')
