import os
import json
import helpers.musicHelper as musicHelper

from Navigation import Navigation
from state.stateEnum import StateEnum

class WordsImporter(Navigation):
    _PREVIOUS_STATE = StateEnum.CONFIG
    LEARN = "aprendizaje"
    EVALUATE = "evaluacion"
    _imported_words = []

    def __init__(self):
        super(WordsImporter, self).__init__()
        musicHelper.play_navigation_sound("words-importer-message")

    def _set_attributes(self):
        super(WordsImporter, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE

    def _select_option(self):
        self._import_words()
        musicHelper.play_navigation_sound("words-importer-ok")
        self._back_to_previous_state()

    def _import_words(self):
        f = open("palabras_a_cargar.txt", "r")
        result_dict = dict()
        line = f.readline()
        
        while line:
            line = line.replace('\n', '').replace('\r', '').replace(':', '')
            if line == self.LEARN:
                result_dict = self._decode_module_words(f, "learn-levels", result_dict)
            elif line == self.EVALUATE:
                result_dict = self._decode_module_words(f, "evaluation-levels", result_dict)
            else:
                raise Exception('Error en formato de archivo de entrada')
            line = f.readline()
        f.close()

        self._write_custom_levels_file(result_dict)
        #musicHelper.generate_word_sounds(self._imported_words) FIXME: Ver si hacerlo

    def _decode_module_words(self, file, module_key, result_dict):
        line = file.readline()
        dict_1 = self._decode_level_words(line)
        line = file.readline()
        dict_2 = self._decode_level_words(line)
        line = file.readline()
        dict_3 = self._decode_level_words(line)

        result_dict[module_key] = [dict_1, dict_2, dict_3]
        return result_dict

    def _decode_level_words(self, level_line):
        my_dict = dict()

        level_line = level_line.split(':')

        if len(level_line) != 2: #Separador : mal usado
            raise Exception('Error en formato de archivo de entrada')

        level_number = level_line[0]
        words_unprocessed = level_line[1].split(',')
        
        if len(words_unprocessed) == 0: #No se utilizo el separador , entre palabras, o esta vacio
            raise Exception('Error en formato de archivo de entrada')
        
        words_processed = []

        for word in words_unprocessed:
            words_processed.append(word.replace(' ', '').replace('\n', '').replace('\r', ''))

        my_dict["id"] = level_number
        my_dict["words"] = words_processed
        self._imported_words.extend(words_processed)
        
        return my_dict

    def _write_custom_levels_file(self, result_dict):
        json_str = json.dumps(result_dict)
        parsed = json.loads(json_str)

        file_to_write = open("config/custom_levels.json", 'w')
        file_to_write.write(json.dumps(parsed, indent=4, sort_keys=True))
        file_to_write.close()