import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state.stateEnum import StateEnum
from helpers import processorHelper
from helpers import configHelper
from BrailleMatrixHandler import BrailleMatrixHandler

class Write(BrailleMatrixHandler):
    _PREVIOUS_STATE = StateEnum.MENU

    def __init__(self):
        super(Write, self).__init__()

    def _set_attributes(self):
        super(Write, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE
    
    def _print_welcome_message(self):
        print("Comienza la escritura libre, toque boton Atras para salir ...")