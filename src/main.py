from Level import Level
import musicPlayer
import helpers.loadingHelper as loadingHelper

from state import state


my_input = loadingHelper.get_input_processer()
my_output = loadingHelper.get_output_processer()

my_output.write('HOLA')

print("Starting!")
letter = "start"

state_object = loadingHelper.get_state_object()

# print(state.set_state('learn-menu'))
# print(state.get_state())

while letter != "bye":
    previous_state = state.get_state()
    #letter = my_input.get_input()
    state_object.process_input(my_input.get_input())
    # musicPlayer.playLetter(letter)
    #print(letter)
    if previous_state != state.get_state():
        state_object = loadingHelper.get_state_object()
    #my_output.write(letter)
