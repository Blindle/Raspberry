import pygame
import os
import sys
import configHelper

sys.path.append(os.path.dirname(__file__) + "/../audios")

pygame.mixer.pre_init(18000, -16, 2, 2048)
pygame.mixer.init()

def play_letter(letter):
    _play_sound("letters", letter.lower())

def play_navigation_sound(sound_name):
    _play_sound("navigation", sound_name)

def play_word(word):
    _play_sound("words", word)

def play_word_spell_out(word):
    for letter in word:
        play_navigation_sound("letter")
        play_letter(letter)
        _play_points(configHelper.get_points(letter))

def _play_points(points):
    play_navigation_sound("points")
    index = 0
    for point in points:
        index += 1
        if point == "1":
            play_letter(str(index))

def _play_sound(folder, sound):
    pygame.mixer.music.load("audios/{}/{}.wav".format(folder, sound))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
    	continue

def play_menu_option(menu_option):
    menu_option = _is_level_number(menu_option)
    play_navigation_sound(menu_option)

def _is_level_number(menu_option):
    if menu_option == 1 or menu_option == 2 or menu_option == 3:
        menu_option = 'level' + str(menu_option)
    return menu_option

def play_enter_action(next_state):
    play_navigation_sound("enter-" + next_state)

def play_back_to_action(prev_state):
    play_navigation_sound("backto-" + prev_state)

def play_end_of_module_action(state, level_number, prev_state):
    play_navigation_sound("end-" + state + "-level" + str(level_number))
    play_back_to_action(prev_state)

def generate_word_sounds(words):
    os.system("rm audios/words/*.wav")
    for word in words:
        _generate_sound("words", word, word)

def generate_navigation_sound(sound_name, speech):
    _generate_sound("navigation", sound_name, speech)

def generate_letter_sounds(letters):
    os.system("rm audios/letters/*.wav")
    for letter in letters:
        _generate_sound("letters", letter, letter)

def _generate_sound(folder, sound_name, speech):
    os.system("pico2wave -w=audios/{}/{}.wav -l='es-ES' '{}'".format(folder, sound_name, speech))