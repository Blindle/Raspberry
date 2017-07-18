import json


class Level:
    def __init__(self, level_number, mode):
        self.level_number = level_number
        with open('data.json') as data_file:
            self.data = json.load(data_file)[
                mode + "-levels"][self.level_number - 1]

    def print_level_number(self):
        print(self.level_number)

    def print_words_in_level(self):
        for word in self.data['words']:
            print(word)
