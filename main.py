from Level import Level
import musicPlayer

from input.console import ConsoleInput
from input.buttons import ButtonsInput
from output.console import ConsoleOutput
from output.arduino import ArduinoOutput
import config.configHelper as configHelper


config = configHelper.getConfig()

if config['input'] == 'console':
    my_input = ConsoleInput()
else:
    my_input = ButtonsInput()

if config['output'] == 'console':
    my_output = ConsoleOutput()
else:
    my_output = ArduinoOutput(9600)

my_output.write('HOLA')

print("Starting!")
letter = "start"

while letter != "bye":
    letter = my_input.get_input()
    # musicPlayer.playLetter(letter)
    print(letter)
    #my_output.write(letter)
