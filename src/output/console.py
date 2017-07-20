class ConsoleOutput:
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
            'O': u'\u2805',
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
            'Z': u'\u2835'
        }.get(character, '')
