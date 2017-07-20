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
from state.objects.LearnMenu import LearnMenu
from state.objects.EvaluateMenu import EvaluateMenu

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
    current_state = state.get_state()
    if current_state == 'menu':
        state_object = MainMenu()
    elif current_state == 'learn-menu':
        state_object = LearnMenu()
    elif current_state == 'evaluate-menu':
        state_object = EvaluateMenu()
    elif current_state == 'learn':
        state_object = 'Learn()'
    elif current_state == 'write':
        state_object = 'Write()'
    elif current_state == 'evaluate':
        state_object = 'Evaluate()'
    elif current_state == 'config':
        state_object = 'Config()'
    else:
        raise Exception('The state isnt valid')

    return state_object

