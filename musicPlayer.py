import pygame

pygame.mixer.init()

def playFile(file_path):
    pygame.mixer.music.load(file_path)
 #   playAudioLoaded()

def playLetter(letter):
    pygame.mixer.music.load("audios/letters/" + letter.lower() + ".mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
    	continue

#def playAudioLoaded():
	