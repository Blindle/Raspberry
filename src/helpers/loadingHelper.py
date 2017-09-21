import sys
import os

sys.path.append(os.path.dirname(__file__) + "../")

from state import state
from state.stateEnum import StateEnum

from state.objects.MainMenu import MainMenu
from state.objects.LearnMenu import LearnMenu
from state.objects.EvaluateMenu import EvaluateMenu
from state.objects.Write import Write
from state.objects.Learn import Learn
from state.objects.Evaluate import Evaluate
from state.objects.ConfigurationMenu import ConfigurationMenu
from state.objects.EngineRegulation import EngineRegulation
from state.objects.WordsImporter import WordsImporter
from state.objects.BlindeSoundsGenerator import BlindeSoundsGenerator
from state.objects.WordSourceSelector import WordSourceSelector

def get_state_object():
    current_state = state.get_state()
    if current_state == StateEnum.MENU.key:
        state_object = MainMenu()
    elif current_state == StateEnum.LEARN_MENU.key:
        state_object = LearnMenu()
    elif current_state == StateEnum.EVALUATE_MENU.key:
        state_object = EvaluateMenu()
    elif current_state == StateEnum.LEARN.key:
        state_object = Learn(state.get_level())
    elif current_state == StateEnum.WRITE.key:
        state_object = Write()
    elif current_state == StateEnum.EVALUATE.key:
        state_object = Evaluate(state.get_level())
    elif current_state == StateEnum.CONFIG.key:
        state_object = ConfigurationMenu()
    elif current_state == StateEnum.REGULATION.key:
        state_object = EngineRegulation()
    elif current_state == StateEnum.WORDS_IMPORTER.key:
        state_object = WordsImporter()
    elif current_state == StateEnum.SOUNDS_GENERATOR.key:
        state_object = BlindeSoundsGenerator()
    elif current_state == StateEnum.WORD_SOURCE.key:
        state_object = WordSourceSelector()
    else:
        raise Exception('The state isnt valid')

    return state_object

