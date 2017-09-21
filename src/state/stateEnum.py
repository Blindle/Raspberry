from enum import Enum

class StateEnum(Enum):
	MENU             = ('menu', 'Menu Principal')
	LEARN_MENU       = ('learn-menu', 'Modo Aprendizaje')
	EVALUATE_MENU    = ('evaluate-menu', 'Modo Evaluacion')
	LEARN            = ('learn', 'Aprendizaje')
	WRITE            = ('write', 'Escritura')
	EVALUATE         = ('evaluate', 'Evaluacion')
	CONFIG           = ('config', 'Configuracion')
	REGULATION       = ('regulation', 'Regulacion de motores')
	WORDS_IMPORTER   = ('words-importer', 'Cargar nuevas palabras')
	SOUNDS_GENERATOR = ('sounds-generator', 'Generar sonidos de Blindle')
	WORD_SOURCE      = ('word-source', 'Fuente de palabras')
	LEVEL_1          = (1, 'Nivel 1')
	LEVEL_2          = (2, 'Nivel 2')
	LEVEL_3          = (3, 'Nivel 3')
	
	def __init__(self, key, real_name):	
		self.key = key 
		self.real_name = real_name