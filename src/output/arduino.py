import serial
from OutputProcessor import OutputProcessor

PORT = 9600

class ArduinoOutput(OutputProcessor):

    _INIT_MSG = "    "

    def __init__(self):
        self.output = serial.Serial('/dev/ttyACM0', PORT)

    def write(self, word):
        sanitized_output = (self._sanitize_word(word)).encode("utf-8")
        self.output.write(sanitized_output)

    def initialize(self):
        self.output.write(self._INIT_MSG)

    def _sanitize_word(self, word):
        if word[0] == 'd':
            return word
        output = list(self._INIT_MSG)
        index = 0
        for letter in word:
            output[index] = letter
            index += 1
        return ''.join(output)

    def __del__(self):
    	self.output.close()