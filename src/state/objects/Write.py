import sys
import os
import helpers.musicHelper as musicHelper
import helpers.usbHelper as usbHelper
sys.path.append(os.path.dirname(__file__) + "../")

from state.stateEnum import StateEnum
from helpers import processorHelper
from helpers import configHelper
from BrailleMatrixHandler import BrailleMatrixHandler

class Write(BrailleMatrixHandler):
    _PREVIOUS_STATE = StateEnum.MENU
    _FILE_NAME = "escritura_blindle"
    _is_coming_out = False

    def __init__(self):
        super(Write, self).__init__()

    def _set_attributes(self):
        super(Write, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE
    
    def _print_welcome_message(self):
        print("Comienza la escritura libre, toque boton Atras para salir ...")

    def process_input(self, input_value):
       if input_value != "back" or self._is_coming_out == True:
           super(Write, self).process_input(input_value)
       else:
           self._is_coming_out = True
           print "Desea guardar los cambios?"
           musicHelper.play_navigation_sound("write-confirmMsg")

    def _select_option(self):
       if self._is_coming_out == True:
           if not usbHelper.is_pendrive_connected():
               print "No hay ningun pendrive conectado. Conecte o toque atras para salir"
               musicHelper.play_navigation_sound("write-error-pendriveDisconnected")
               return
            
           self._save_in_txt()
           print "Guardado con exito"
           musicHelper.play_navigation_sound("write-saveOk")
           super(Write, self)._back_to_previous_state()

    def _save_in_txt(self):
        written_text = self._transform_points_into_symbols(self._current_letters_size).lower()
        written_text = written_text + "\n"
        usbHelper.save_txt_file_in_pendrive(self._FILE_NAME, written_text)