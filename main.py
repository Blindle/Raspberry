from Level import Level
import musicPlayer
import serial

mode = 'evaluation'
level = Level(1, mode)

level.print_words_in_level()

#musicPlayer.play("audio.mp3")



arduino = serial.Serial('/dev/ttyACM0', 9600)

print("Starting!")
comando = "start"

while != "bye":
      comando = raw_input('Introduce un letra: ') #Input
      arduino.write(comando) #Mandar un comando hacia Arduino
      print("letra enviada: " + comando)

arduino.close() #Finalizamos la comunicacion