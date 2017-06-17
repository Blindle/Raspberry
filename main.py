from Level import Level
import musicPlayer
import serial

mode = 'evaluation'
level = Level(1, mode)

level.print_words_in_level()

#musicPlayer.play("audio.mp3")



arduino = serial.Serial('/dev/ttyACM0', 9600)

print("Starting!")

while True:
      comando = raw_input('Introduce un comando: ') #Input
      arduino.write(comando) #Mandar un comando hacia Arduino
      if comando == 'H':
            print('LED ENCENDIDO')
      elif comando == 'L':
            print('LED APAGADO')

arduino.close() #Finalizamos la comunicacion