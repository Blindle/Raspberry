import serial
from OutputProcessor import OutputProcessor

PORT = 9600

class ArduinoOutput(OutputProcessor):
    def __init__(self):
        self.output = serial.Serial('/dev/ttyACM0', PORT)

    def write(self, word):
    	self.output.write(word)

    def __del__(self):
    	self.output.close()