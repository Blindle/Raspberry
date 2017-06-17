from Level import Level
import musicPlayer
import serial

mode = 'evaluation'
level = Level(1, mode)

level.print_words_in_level()

#musicPlayer.play("audio.mp3")



arduino = serial.Serial('/dev/ttyACM0', 9600)

print("Starting!")
letter = "start"

while letter != "bye":
      letter = raw_input('Introduce un letra: ') #Input
      arduino.write(letter) #Mandar un comando hacia Arduino
      musicPlayer.playLetter(letter)
      print("letra enviada: " + letter)

arduino.close() #Finalizamos la comunicacion
