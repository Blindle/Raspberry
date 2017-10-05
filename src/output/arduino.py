import serial
from OutputProcessor import OutputProcessor

PORT = 9600

class ArduinoOutput(OutputProcessor):

    _INIT_MSG = "        "

    def __init__(self):
        self.output = serial.Serial('/dev/ttyACM0', PORT)

    def write(self, word):
    	self.output.write(word.encode("utf-8"))

    def initialize(self):
        self.output.write(self._INIT_MSG)

    def __del__(self):
    	self.output.close()