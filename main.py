from Level import Level
import musicPlayer

from input.console import ConsoleInput
from input.buttons import ButtonsInput
from output.console import ConsoleOutput
from output.arduino import ArduinoOutput

console_input = True
console_output = True

if console_input == True:
	my_input = ConsoleInput()
else:
	my_input = ButtonsInput()

if console_output == True:
	my_output = ConsoleOutput()
else:
	my_output = ArduinoOutput()


print("Starting!")
letter = "start"

while letter != "bye":
      letter = my_input.get_input()
      musicPlayer.playLetter(letter)
      my_output.write(letter)
      print("letra enviada: " + letter)
