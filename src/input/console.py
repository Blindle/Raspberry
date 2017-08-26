import click
from InputProcessor import InputProcessor


class ConsoleInput(InputProcessor):
    def __init__(self):
        pass

    def get_input(self):
        cInput = self._process_input(click.getchar())
        while cInput == '':
            cInput = self._process_input(click.getchar())
        return cInput

    def __del__(self):
        pass

    def _process_input(self, cInput):
        return {
            u'\x1b[A': 'up',
            u'\x1b[B': 'down',
            u'\x1b[C': 'right',
            u'\x1b[D': 'left',
            u'\r': 'enter',
            u'\x7f': 'back',
            'a': 1,
            's': 2,
            'd': 3,
            'j': 4,
            'k': 5,
            'l': 6
        }.get(cInput, '')
