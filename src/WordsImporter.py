import os
import json

class WordsImporter():
    
    LEARN = "aprendizaje"
    EVALUATE = "evaluacion"

    def import_words(self):
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
                print("ERROR")
            line = f.readline()
        f.close()
        self._write_custom_levels_file(result_dict)

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
        level_number = level_line[0]

        if level_number in my_dict:
            print("El nivel " + level_number + " esta duplicado.")

        words_unprocessed = level_line[1].split(',')
        words_processed = []
        for word in words_unprocessed:
            words_processed.append(word.replace(' ', '').replace('\n', '').replace('\r', ''))

        my_dict["id"] = level_number
        my_dict["words"] = words_processed

        return my_dict

    def _write_custom_levels_file(self, result_dict):
        json_str = json.dumps(result_dict)
        parsed = json.loads(json_str)

        file_to_write = open("config/custom_levels.json", 'w')
        file_to_write.write(json.dumps(parsed, indent=4, sort_keys=True))
        file_to_write.close()