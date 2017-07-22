import helpers.loadingHelper as loadingHelper
import helpers.processorHelper as processorHelper

from state import state

my_input = processorHelper.get_input_processor()
my_output = processorHelper.get_output_processor()

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
