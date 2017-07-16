#import msvcrt

class ConsoleInput:
    def __init__(self):
    	pass

    def get_input(self):
    	return input('Introduce un letra: ')
    	#return msvcrt.getch()

    def __del__(self):
    	pass