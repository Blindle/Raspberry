import helpers.loadingHelper as loadingHelper
import helpers.processorHelper as processorHelper
import helpers.musicHelper as musicHelper

from state import state

input_processor = processorHelper.get_input_processor()
output_processor = processorHelper.get_output_processor()

output_processor.write('HOLA')

print("Starting!")
my_input = "start"

musicHelper.play_navigation_sound("welcomeMessage")

state_object = loadingHelper.get_state_object()

# print(state.set_state('learn-menu'))
# print(state.get_state())

while my_input != "bye":
    previous_state = state.get_state()
    my_input = input_processor.get_input()
    state_object.process_input(my_input)
    # musicPlayer.playLetter(letter)
    #print(letter)
    if previous_state != state.get_state():
        state_object = loadingHelper.get_state_object()
        
    #my_output.write(letter)
