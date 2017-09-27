# coding=utf-8
import os
import helpers.musicHelper as musicHelper
import helpers.configHelper as configHelper

from Navigation import Navigation
from state.stateEnum import StateEnum

class BlindeSoundsGenerator(Navigation):
    _PREVIOUS_STATE = StateEnum.CONFIG

    def __init__(self):
        super(BlindeSoundsGenerator, self).__init__()
        musicHelper.play_navigation_sound("sounds-generator-message")
    
    def _set_attributes(self):
        super(BlindeSoundsGenerator, self)._set_attributes()
        self._previous_state = self._PREVIOUS_STATE

    def _select_option(self):
        self._generate_navigation_sounds()
        self._generate_default_words_sounds()
        self._generate_letters_sounds()
        musicHelper.play_navigation_sound("sounds-generator-ok")
        self._back_to_previous_state()

    def _generate_default_words_sounds(self):
        level_words = []
        #FIXME: Arreglar para que traiga unicamente las palabras por default
        level_words.extend(configHelper.get_level_config("learn", 1)['words'])
        level_words.extend(configHelper.get_level_config("learn", 2)['words'])
        level_words.extend(configHelper.get_level_config("learn", 3)['words'])
        level_words.extend(configHelper.get_level_config("evaluation", 1)['words'])
        level_words.extend(configHelper.get_level_config("evaluation", 2)['words'])
        level_words.extend(configHelper.get_level_config("evaluation", 3)['words'])
        musicHelper.generate_default_word_sounds(level_words)

    def _generate_navigation_sounds(self):
        os.system("rm audios/navigation/*.wav")

        # Learn Module
        musicHelper.generate_navigation_sound("learn-menu", "Modo Aprendizaje")
        musicHelper.generate_navigation_sound("enter-learn-menu", "Entrando al menú de aprendizaje. Seleccione un nivel")
        musicHelper.generate_navigation_sound("enter-learn-level1", "Entrando al nivel 1 de aprendizaje")
        musicHelper.generate_navigation_sound("enter-learn-level2", "Entrando al nivel 2 de aprendizaje")
        musicHelper.generate_navigation_sound("enter-learn-level3", "Entrando al nivel 3 de aprendizaje")
        musicHelper.generate_navigation_sound("end-learn-level1", "Nivel 1 de aprendizaje finalizado")
        musicHelper.generate_navigation_sound("end-learn-level2", "Nivel 2 de aprendizaje finalizado")
        musicHelper.generate_navigation_sound("end-learn-level3", "Nivel 3 de aprendizaje finalizado")
        musicHelper.generate_navigation_sound("backto-learn-menu", "Regresando al menú de aprendizaje")
        musicHelper.generate_navigation_sound("points", "Puntos")

        # Write Module
        musicHelper.generate_navigation_sound("write", "Escritura libre")
        musicHelper.generate_navigation_sound("enter-write", "Comienza la escritura libre, toque el botón atras para salir")
        musicHelper.generate_navigation_sound("write-confirmMsg", "Si desea guardar toque Enter, sino toque Atrás")
        musicHelper.generate_navigation_sound("write-saveOk", "Archivo guardado correctamente")
        musicHelper.generate_navigation_sound("write-error-pendriveDisconnected", "Conecte un pendraiv y toque Enter. Si desea salir toque Atrás.")

        # Evaluate Module
        musicHelper.generate_navigation_sound("evaluate-menu", "Modo Evaluación")
        musicHelper.generate_navigation_sound("enter-evaluate-menu", "Entrando al menú de evaluación. Seleccione un nivel")
        musicHelper.generate_navigation_sound("enter-evaluate-level1", "Entrando al nivel 1 de evaluación")
        musicHelper.generate_navigation_sound("enter-evaluate-level2", "Entrando al nivel 2 de evaluación")
        musicHelper.generate_navigation_sound("enter-evaluate-level3", "Entrando al nivel 3 de evaluación")
        musicHelper.generate_navigation_sound("end-evaluate-level1", "Nivel 1 de evaluación finalizado")
        musicHelper.generate_navigation_sound("end-evaluate-level2", "Nivel 2 de evaluación finalizado")
        musicHelper.generate_navigation_sound("end-evaluate-level3", "Nivel 3 de evaluación finalizado")
        musicHelper.generate_navigation_sound("backto-evaluate-menu", "Regresando al menú de evaluación")
        musicHelper.generate_navigation_sound("evaluate-representMessage", "La palabra que se debe representar es")
        musicHelper.generate_navigation_sound("evaluate-nextWord", "Se pasa a la siguiente palabra")
        musicHelper.generate_navigation_sound("evaluate-correctMessage", "Palabra escrita correctamente.")
        musicHelper.generate_navigation_sound("evaluate-errorMessage", "Palabra escrita incorrectamente.")
        musicHelper.generate_navigation_sound("evaluate-maxCantErrorsMessage", "Cometiste tres errores.")
        musicHelper.generate_navigation_sound("evaluate-result", "Resultado de la evaluación")
        musicHelper.generate_navigation_sound("letter", "Letra")
        musicHelper.generate_navigation_sound("word", "Palabra")
        musicHelper.generate_navigation_sound("mistakes", "Errores")

        # Configuration
        musicHelper.generate_navigation_sound("config", "Configuración")
        musicHelper.generate_navigation_sound("enter-config", "Entrando a la configuración")
        musicHelper.generate_navigation_sound("backto-config", "Regresando a Configuración")

        # Engine Regulation
        musicHelper.generate_navigation_sound("regulation", "Regular motores")
        musicHelper.generate_navigation_sound("enter-regulation", "Entrando a la regulación de los motores")
        musicHelper.generate_navigation_sound("motor1", "Motor 1")
        musicHelper.generate_navigation_sound("motor2", "Motor 2")
        musicHelper.generate_navigation_sound("motor3", "Motor 3")
        musicHelper.generate_navigation_sound("motor4", "Motor 4")
        musicHelper.generate_navigation_sound("motor5", "Motor 5")
        musicHelper.generate_navigation_sound("motor6", "Motor 6")
        musicHelper.generate_navigation_sound("motor7", "Motor 7")
        musicHelper.generate_navigation_sound("motor8", "Motor 8")
        musicHelper.generate_navigation_sound("move-L", "Moviendo hacia la izquierda")
        musicHelper.generate_navigation_sound("move-R", "Moviendo hacia la derecha")

        # Word Source
        musicHelper.generate_navigation_sound("word-source", "Fuente de palabras")
        musicHelper.generate_navigation_sound("enter-word-source", "Entrando a fuente de palabras")
        musicHelper.generate_navigation_sound("word-source-message", "Seleccione la fuente de palabras, toque enter para confirmar. La fuente actual es")
        musicHelper.generate_navigation_sound("word-source-default", "Por defecto")
        musicHelper.generate_navigation_sound("word-source-custom", "Personalizada")
        musicHelper.generate_navigation_sound("word-source-selection", "Ha seleccionado la fuente de palabras")
        
        # Words Importer
        musicHelper.generate_navigation_sound("words-importer", "Cargar nuevas palabras")
        musicHelper.generate_navigation_sound("enter-words-importer", "Entrando a la carga de nuevas palabras")
        musicHelper.generate_navigation_sound("words-importer-message", "Pulse el botón enter para comenzar con la carga de palabras")
        musicHelper.generate_navigation_sound("words-importer-ok", "Carga de palabras exitosa")
        musicHelper.generate_navigation_sound("words-importer-error", "Hubo un error en la carga de palabras")
        
        # Sounds Generator
        musicHelper.generate_navigation_sound("sounds-generator", "Generar sonidos de Bláindel")
        musicHelper.generate_navigation_sound("enter-sounds-generator", "Entrando a la generación de sonidos de Bláindel")
        musicHelper.generate_navigation_sound("sounds-generator-message", "Pulse el botón enter para generar los sonidos por defecto")
        musicHelper.generate_navigation_sound("sounds-generator-ok", "Generación de sonidos exitosa")

        # Levels
        musicHelper.generate_navigation_sound("level1", "Nivel 1")
        musicHelper.generate_navigation_sound("level2", "Nivel 2")
        musicHelper.generate_navigation_sound("level3", "Nivel 3")

        #Others
        musicHelper.generate_navigation_sound("welcomeMessage", "Bienvenido a Bláindel")
        musicHelper.generate_navigation_sound("backto-menu", "Regresando al menú principal")

    def _generate_letters_sounds(self):
        letters = []
        letters.extend('a')
        letters.extend('b')
        letters.extend('c')
        letters.extend('d')
        letters.extend('e')
        letters.extend('f')
        letters.extend('g')
        letters.extend('h')
        letters.extend('i')
        letters.extend('j')
        letters.extend('k')
        letters.extend('l')
        letters.extend('m')
        letters.extend('n')
        letters.extend('ñ')
        letters.extend('o')
        letters.extend('p')
        letters.extend('q')
        letters.extend('r')
        letters.extend('s')
        letters.extend('t')
        letters.extend('u')
        letters.extend('v')
        letters.extend('w')
        letters.extend('x')
        letters.extend('y')
        letters.extend('z')
        letters.extend('0')
        letters.extend('1')
        letters.extend('2')
        letters.extend('3')
        letters.extend('4')
        letters.extend('5')
        letters.extend('6')
        letters.extend('7')
        letters.extend('8')
        letters.extend('9')
        musicHelper.generate_letter_sounds(letters)