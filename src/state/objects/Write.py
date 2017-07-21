import sys
import os
sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum

class Write:

    def __init__(self):
        print("Comienza la escritura libre, toque boton Atras para salir ...")

    def process_input(self, input_value):

        if input_value == "back":
            print("Regresando a " + StateEnum.MENU.realName)
            state.set_state(StateEnum.MENU)

    def _verify_overflow(self):
        pass