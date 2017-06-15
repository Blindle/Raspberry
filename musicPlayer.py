import pygame

pygame.mixer.init()

def play(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue