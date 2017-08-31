import pygame
import os
import sys

sys.path.append(os.path.dirname(__file__) + "/../audios")

pygame.mixer.pre_init(18000, -16, 2, 2048)
pygame.mixer.init()

def play_word(word):
    for letter in word:
        _play_letter(letter)

def _play_letter(letter):
    pygame.mixer.music.load("audios/letters/" + letter.lower() + ".mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
    	continue

def play_menu_option(menu_option):
    menu_option = _is_level_number(menu_option)
    play_navigation_sound(menu_option)

def play_enter_action(state):
    play_navigation_sound("enter-" + state)

def play_back_to_action(state):
    play_navigation_sound("backto-" + state)

def play_navigation_sound(sound_name):
    pygame.mixer.music.load("audios/navigation/" + sound_name + ".wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
    	continue

def _is_level_number(menu_option):
    if menu_option == 1 or menu_option == 2 or menu_option == 3:
        menu_option = 'level' + str(menu_option)
    return menu_option