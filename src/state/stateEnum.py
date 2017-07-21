from enum import Enum

class StateEnum(Enum):
	MENU          = ('menu', 'Menu Principal')
	LEARN_MENU    = ('learn-menu', 'Modo Aprendizaje')
	EVALUATE_MENU = ('evaluate-menu', 'Modo Evaluacion')
	LEARN         = ('learn', 'Aprendizaje')
	WRITE         = ('write', 'Escritura')
	EVALUATE      = ('evaluate', 'Evaluacion')
	CONFIG        = ('config', 'Configuracion')
	LEVEL_1       = ('level1', 'Nivel 1')
	LEVEL_2       = ('level2', 'Nivel 2')
	LEVEL_3       = ('level3', 'Nivel 3')
	
	def __init__(self, key, realName):	
		self.key = key 
		self.realName = realName 