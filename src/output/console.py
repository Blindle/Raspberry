from OutputProcessor import OutputProcessor

class ConsoleOutput(OutputProcessor):
    def __init__(self):
        pass

    def write(self, word):
        print(self._createPrintingString(word))

    def __del__(self):
        pass

    def _createPrintingString(self, word):
        string = ''
        for c in str(word):
            string = string + ' ' + self._getUnicode(c)
        return string

    def _getUnicode(self, character):
        return {
            'A': u'\u2801',
            'B': u'\u2803',
            'C': u'\u2809',
            'D': u'\u2819',
            'E': u'\u2811',
            'F': u'\u280B',
            'G': u'\u281B',
            'H': u'\u2813',
            'I': u'\u280A',
            'J': u'\u281A',
            'K': u'\u2805',
            'L': u'\u2807',
            'M': u'\u280D',
            'N': u'\u281D',
            'O': u'\u2815',
            'P': u'\u280F',
            'Q': u'\u281F',
            'R': u'\u2817',
            'S': u'\u280E',
            'T': u'\u281E',
            'U': u'\u2825',
            'V': u'\u2827',
            'W': u'\u283A',
            'X': u'\u282D',
            'Y': u'\u283D',
            'Z': u'\u2835',
            '0': u'\u2800',
            '_': u'\u2824',
            '-': u'\u2818',
            ',': u'\u2802',
            ';': u'\u281C',
            '5': u'\u2831',
            ':': u'\u2820',
            '6': u'\u2833',
            '!': u'\u2816',
            '\'': u'\u282E',
            '?': u'\u2826',
            '1': u'\u282F',
            '.': u'\u2832',
            '"': u'\u2822',
            '(': u'\u282A',
            ')': u'\u282B',
            '[': u'\u2808',
            ']': u'\u2810',
            '{': u'\u2812',
            '}': u'\u2814',
            '@': u'\u2834',
            '*': u'\u2821',
            '/': u'\u280C',
            '\\': u'\u282C',
            '&': u'\u2829',
            '#': u'\u283C',
            '%': u'\u2828',
            '^': u'\u2839',
            '2': u'\u283B',
            '3': u'\u2837',
            '<': u'\u2804',
            '>': u'\u2806',
            '4': u'\u2838',
            '|': u'\u2836',
            '~': u'\u2830',
            '$': u'\u2823',
            '+': u'\u283E',
            '7': u'\u283F'
        }.get(character, '')
