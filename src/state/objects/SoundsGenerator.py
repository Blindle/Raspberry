# coding=utf-8
import os
import helpers.musicHelper as musicHelper
import helpers.configHelper as configHelper

from Processor import Processor
from state.stateEnum import StateEnum

class SoundsGenerator(Processor):
    _PREVIOUS_STATE = StateEnum.CONFIG

    def __init__(self):
        super(SoundsGenerator, self).__init__()
        musicHelper.play_navigation_sound("sounds-generator-message")
    
    def _set_attributes(self):
        super(SoundsGenerator, self)._set_attributes()
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
        musicHelper.generate_navigation_sound("enter-write", "Comienza la escritura libre, toque el botón atrás para salir")
        musicHelper.generate_navigation_sound("write-confirmMsg", "Si desea guardar toque Aceptar, sino toque atrás")
        musicHelper.generate_navigation_sound("write-saveOk", "Archivo guardado!")
        musicHelper.generate_navigation_sound("write-error-pendriveDisconnected", "Conecte un pendraiv y toque Aceptar. Si desea salir toque Atrás")

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
        musicHelper.generate_navigation_sound("evaluate-representMessage", "Se debe representar")
        musicHelper.generate_navigation_sound("evaluate-nextWord", "Se pasa a la siguiente palabra")
        musicHelper.generate_navigation_sound("evaluate-correctMessage", "Palabra escrita con éxito")
        musicHelper.generate_navigation_sound("evaluate-errorMessage", "Palabra mal escrita")
        musicHelper.generate_navigation_sound("evaluate-maxNumberErrorsMessage", "Cometiste tres errores")
        musicHelper.generate_navigation_sound("evaluate-result", "Resultado al menù de Evaluación")
        musicHelper.generate_navigation_sound("letterExplanation", "Letra")
        musicHelper.generate_navigation_sound("wordExplanation", "Palabra")
        musicHelper.generate_navigation_sound("mistakes", "Errores")

        # Configuration
        musicHelper.generate_navigation_sound("config", "Configuración")
        musicHelper.generate_navigation_sound("enter-config", "Entrando a la configuración")
        musicHelper.generate_navigation_sound("backto-config", "Regresando a Configuración")

        # Engine Regulation
        musicHelper.generate_navigation_sound("regulation", "Regular motores")
        musicHelper.generate_navigation_sound("enter-regulation", "Entrando a la regulación de los motores")
        musicHelper.generate_navigation_sound("regulation-message", "El boton 1 mueve el motor hacia la izquierda y el 6 a la derecha")
        musicHelper.generate_navigation_sound("motor1", "Motor 1")
        musicHelper.generate_navigation_sound("motor2", "Motor 2")
        musicHelper.generate_navigation_sound("motor3", "Motor 3")
        musicHelper.generate_navigation_sound("motor4", "Motor 4")
        musicHelper.generate_navigation_sound("motor5", "Motor 5")
        musicHelper.generate_navigation_sound("motor6", "Motor 6")
        musicHelper.generate_navigation_sound("motor7", "Motor 7")
        musicHelper.generate_navigation_sound("motor8", "Motor 8")

        # Word Source
        musicHelper.generate_navigation_sound("word-source", "Fuente de palabras")
        musicHelper.generate_navigation_sound("enter-word-source", "Entrando a fuente de palabras")
        musicHelper.generate_navigation_sound("word-source-message", "Seleccione la fuente de palabras, toque aceptar para confirmar. La fuente actual es")
        musicHelper.generate_navigation_sound("word-source-default", "Por defecto")
        musicHelper.generate_navigation_sound("word-source-custom", "Personalizada")
        musicHelper.generate_navigation_sound("word-source-options", "Las opciones son")
        musicHelper.generate_navigation_sound("word-source-selection", "Ha seleccionado la fuente de palabras")
        musicHelper.generate_navigation_sound("word-source-customNotExists", "No se cargaron niveles personalizados. Seleccione los niveles por defecto o cargue nuevas palabras.")
        
        # Words Importer
        musicHelper.generate_navigation_sound("words-importer", "Cargar nuevas palabras")
        musicHelper.generate_navigation_sound("enter-words-importer", "Entrando a la carga de nuevas palabras")
        musicHelper.generate_navigation_sound("words-importer-message", "Pulse el botón Aceptar para comenzar con la carga de palabras")
        musicHelper.generate_navigation_sound("words-importer-ok", "Carga de palabras exitosa")
        musicHelper.generate_navigation_sound("words-importer-error", "Hubo un error en la carga de palabras")
        musicHelper.generate_navigation_sound("words-importer-retry", "Conecte el pendraiv y toque Aceptar para continuar, o toque Atrás para salir.")
        
        # Sounds Generator
        musicHelper.generate_navigation_sound("sounds-generator", "Generar sonidos")
        musicHelper.generate_navigation_sound("enter-sounds-generator", "Entrando a la generación de sonidos")
        musicHelper.generate_navigation_sound("sounds-generator-message", "Pulse el botón aceptar para generar los sonidos por defecto")
        musicHelper.generate_navigation_sound("sounds-generator-ok", "Generación de sonidos exitosa")

        # Levels
        musicHelper.generate_navigation_sound("level1", "Nivel 1")
        musicHelper.generate_navigation_sound("level2", "Nivel 2")
        musicHelper.generate_navigation_sound("level3", "Nivel 3")

        # Exceptions
        musicHelper.generate_exception_sound("file-not-found", "No se encontró el archivo necesario en el pendraiv conectado")
        musicHelper.generate_exception_sound("format", "Formato del archivo incorrecto")
        musicHelper.generate_exception_sound("pendrive-dissconected", "Pendraiv desconectado")

        # Others
        musicHelper.generate_navigation_sound("welcomeMessage", "Bienvenido a Bláindel")
        musicHelper.generate_navigation_sound("backto-menu", "Regresando al menú principal")

        # Word Spelling
        musicHelper.generate_navigation_sound("word-spelling", "Deletreo de palabras")
        musicHelper.generate_navigation_sound("enter-word-spelling", "Entrando a configuración de deletreo de palabras")
        musicHelper.generate_navigation_sound("word-spelling-message", "Seleccione la opción deseada, toque aceptar para confirmar. La configuración actual es")
        musicHelper.generate_navigation_sound("word-spelling-enabled", "Habilitada")
        musicHelper.generate_navigation_sound("word-spelling-disabled", "Deshabilitada")
        musicHelper.generate_navigation_sound("word-spelling-options", "Las opciones son")
        musicHelper.generate_navigation_sound("word-spelling-selection", "Ha seleccionado la opción")

    def _generate_letters_sounds(self):
        os.system("rm audios/letters/*.wav")
        musicHelper.generate_letter_sound("a", "a")
        musicHelper.generate_letter_sound("b", "be larga")
        musicHelper.generate_letter_sound("c", "ce")
        musicHelper.generate_letter_sound("d", "de")
        musicHelper.generate_letter_sound("e", "e")
        musicHelper.generate_letter_sound("f", "efe")
        musicHelper.generate_letter_sound("g", "ge")
        musicHelper.generate_letter_sound("h", "ache")
        musicHelper.generate_letter_sound("i", "i")
        musicHelper.generate_letter_sound("j", "jota")
        musicHelper.generate_letter_sound("k", "ka")
        musicHelper.generate_letter_sound("l", "ele")
        musicHelper.generate_letter_sound("m", "eme")
        musicHelper.generate_letter_sound("n", "ene")
        musicHelper.generate_letter_sound("o", "o")
        musicHelper.generate_letter_sound("p", "pe")
        musicHelper.generate_letter_sound("q", "ku")
        musicHelper.generate_letter_sound("r", "erre")
        musicHelper.generate_letter_sound("s", "ese")
        musicHelper.generate_letter_sound("t", "te")
        musicHelper.generate_letter_sound("u", "u")
        musicHelper.generate_letter_sound("v", "ve corta")
        musicHelper.generate_letter_sound("w", "doble ve")
        musicHelper.generate_letter_sound("x", "equis")
        musicHelper.generate_letter_sound("y", "i griega")
        musicHelper.generate_letter_sound("z", "zeta")
        musicHelper.generate_letter_sound("z", "zeta")
        musicHelper.generate_letter_sound("0", "cero")
        musicHelper.generate_letter_sound("1", "uno")
        musicHelper.generate_letter_sound("2", "dos")
        musicHelper.generate_letter_sound("3", "tres")
        musicHelper.generate_letter_sound("4", "cuatro")
        musicHelper.generate_letter_sound("5", "cinco")
        musicHelper.generate_letter_sound("6", "seis")
        musicHelper.generate_letter_sound("7", "siete")
        musicHelper.generate_letter_sound("8", "ocho")
        musicHelper.generate_letter_sound("9", "nueve")