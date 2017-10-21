import serial
from OutputProcessor import OutputProcessor

PORT = 9600

class ArduinoOutput(OutputProcessor):

    _INIT_MSG = "    "
    _ARDUINO_RESPONSE = "ARDUINO-LISTENING"
    _END_OF_LINE = "z"
    _SLEEP_TIME = 0.1

    def __init__(self):
        self.output = serial.Serial('/dev/ttyACM0', PORT)

    def write(self, word):
        sanitized_output = (self._sanitize_word(word)).encode("utf-8")
        self.output.write(sanitized_output)
        arduino_response = self._readline() #Arduino envia mismo caracter que recibio
        arduino_response = self._readline() #Arduino envia que termino de representar
        if arduino_response != self._ARDUINO_RESPONSE:
            print "Error grave, por favor reinicie el dispostivo."


    def initialize(self):
        self.write(self._INIT_MSG)

    def _sanitize_word(self, word):
        output = list(self._INIT_MSG)
        index = 0
        for letter in word:
            output[index] = letter
            index += 1
        return ''.join(output)

    def __del__(self):
    	self.output.close()

    def _readline(self):
        buffer = ""
        end_of_line_size = len(self._END_OF_LINE)
        while buffer[-end_of_line_size:] != self._END_OF_LINE:
            buffer += self.output.read()
        return buffer.replace(self._END_OF_LINE, '')