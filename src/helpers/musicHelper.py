#import pygame
import os
import sys
import pyglet

sys.path.append(os.path.dirname(__file__) + "/../audios/letters")

pyglet.options['audio'] = ('openal', 'pulse', 'silent')
player = pyglet.media.Player()

#pygame.mixer.init()

def play_file(file_path):
    pass
    #pygame.mixer.music.load(file_path)
 #   playAudioLoaded()

def play_word(word):
    #CHANNEL.stop()

    # pygame.mixer.music.load(os.path.dirname(__file__) + "/../audios/letters/a.mp3")
    # pygame.mixer.music.play()
    # pygame.mixer.music.queue(os.path.dirname(__file__) + "/../audios/letters/e.mp3")

    # pygame.mixer.music.stop()
    first = True
    for letter in word:
        path = str(os.path.dirname(__file__) + "/../audios/letters/" + letter.lower() + ".mp3")
        src = pyglet.media.load(path, streaming=False)
        player.queue(src)
        # if first:
            # first = False
            # pygame.mixer.music.load(os.path.dirname(__file__) + "/../audios/letters/" + letter.lower() + ".mp3")
            #pygame.mixer.music.play()
        # else:
            # pygame.mixer.music.queue(os.path.dirname(__file__) + "/../audios/letters/" + letter.lower() + ".mp3")
        #_play_letter(letter)
        # pygame.mixer.music.play()
    
    player.play()

def _play_letter(letter):
    pass
    #pygame.mixer.music.load("audios/letters/" + letter.lower() + ".mp3")
    #pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy() == True:
    #	continue

#def playAudioLoaded():
	