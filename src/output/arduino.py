# coding=utf-8
import serial
import time
from OutputProcessor import OutputProcessor

PORT = 9600

class ArduinoOutput(OutputProcessor):

    _INIT_MSG = "        "
    _ARDUINO_RESPONSE = "ARDUINO-LISTENING"
    _END_OF_LINE = "z"
    _SLEEP_TIME = 0.1

    def __init__(self):
        self.output = serial.Serial('/dev/ttyACM0', PORT)

    def write(self, word):
    	self.output.write(word.encode("utf-8"))
        arduino_response = self._readline()
        print "Caracter enviado: {} - Caracter recibido: {}".format(word, arduino_response)
        arduino_response = self._readline()
        print "Motores representados: " + arduino_response
        if arduino_response != self._ARDUINO_RESPONSE:
            print "Error grave, por favor reinicie el dispostivo."

    def initialize(self):
        self.output.write(self._INIT_MSG)

    def __del__(self):
    	self.output.close()

    def _readline(self):
        buffer = ""
        end_of_line_size = len(self._END_OF_LINE)
        while buffer[-end_of_line_size:] != self._END_OF_LINE:
            buffer += self.output.read()
        return buffer.replace(self._END_OF_LINE, '')