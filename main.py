from Level import Level
import musicPlayer

mode = 'evaluation'
level = Level(1, mode)

level.print_words_in_level()

musicPlayer.play("audio.mp3")
