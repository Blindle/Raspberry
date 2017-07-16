import serial

class ArduinoOutput:
    def __init__(self, port):
        self.port = port
        self.output = serial.Serial('/dev/ttyACM0', port)

    def write(self, word):
    	self.output.write(word)

    def __del__(self):
    	self.output.close()