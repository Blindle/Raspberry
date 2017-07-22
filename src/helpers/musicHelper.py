import pygame
import os
import sys

sys.path.append(os.path.dirname(__file__) + "/../audios/letters")

pygame.mixer.init()

def play_word(word):
    for letter in word:
        _play_letter(letter)

def _play_letter(letter):
    pygame.mixer.music.load("audios/letters/" + letter.lower() + ".mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
    	continue

	