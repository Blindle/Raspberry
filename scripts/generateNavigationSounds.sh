cd ../src/audios/navigation
rm *.wav
pico2wave -w=welcomeMessage.wav -l='es-ES' '¡Bienvenido a Blindle!'

pico2wave -w=learn-menu.wav -l='es-ES' 'Modo Aprendizaje'
pico2wave -w=write.wav -l='es-ES' 'Escritura libre'
pico2wave -w=evaluate-menu.wav -l='es-ES' 'Modo Evaluación'
pico2wave -w=config.wav -l='es-ES' 'Configuración'

pico2wave -w=level1.wav -l='es-ES' 'Nivel 1'
pico2wave -w=level2.wav -l='es-ES' 'Nivel 2'
pico2wave -w=level3.wav -l='es-ES' 'Nivel 3'

pico2wave -w=enter-learn-menu.wav -l='es-ES' 'Entrando al menú de aprendizaje. Seleccione un nivel'
pico2wave -w=enter-evaluate-menu.wav -l='es-ES' 'Entrando al menú de evaluación. Seleccione un nivel'
pico2wave -w=enter-write.wav -l='es-ES' 'Comienza la escritura libre, toque el boton atras para salir'
pico2wave -w=enter-config.wav -l='es-ES' 'Entrando a la configuración'

pico2wave -w=backto-menu.wav -l='es-ES' 'Regresando al menú principal'

pico2wave -w=enter-learn-level1.wav -l='es-ES' 'Entrando al nivel 1 de aprendizaje'
pico2wave -w=enter-learn-level2.wav -l='es-ES' 'Entrando al nivel 2 de aprendizaje'
pico2wave -w=enter-learn-level3.wav -l='es-ES' 'Entrando al nivel 3 de aprendizaje'

pico2wave -w=end-learn-level1.wav -l='es-ES' 'Nivel 1 de aprendizaje finalizado'
pico2wave -w=end-learn-level2.wav -l='es-ES' 'Nivel 2 de aprendizaje finalizado'
pico2wave -w=end-learn-level3.wav -l='es-ES' 'Nivel 3 de aprendizaje finalizado'
pico2wave -w=backto-learn-menu.wav -l='es-ES' 'Regresando al menú de aprendizaje'

pico2wave -w=enter-evaluate-level1.wav -l='es-ES' 'Entrando al nivel 1 de evaluación'
pico2wave -w=enter-evaluate-level2.wav -l='es-ES' 'Entrando al nivel 2 de evaluación'
pico2wave -w=enter-evaluate-level3.wav -l='es-ES' 'Entrando al nivel 3 de evaluación'

pico2wave -w=end-evaluate-level1.wav -l='es-ES' 'Nivel 1 de evaluación finalizado'
pico2wave -w=end-evaluate-level2.wav -l='es-ES' 'Nivel 2 de evaluación finalizado'
pico2wave -w=end-evaluate-level3.wav -l='es-ES' 'Nivel 3 de evaluación finalizado'
pico2wave -w=backto-evaluate-menu.wav -l='es-ES' 'Regresando al menú de evaluación'

pico2wave -w=evaluate-representMessage.wav -l='es-ES' 'La palabra que se debe representar es'
pico2wave -w=evaluate-nextWord.wav -l='es-ES' 'La palabra fue escrita correctamente. Se pasa a la siguiente palabra'
pico2wave -w=evaluate-errorMessage.wav -l='es-ES' 'Escribiste mal capo, ponéla de vuelta'
pico2wave -w=evaluate-nextWordWithError.wav -l='es-ES' 'Se pasa a la siguiente palabra porque fallaste tres veces'

cd ../letters
rm *.wav
pico2wave -w=a.wav -l='es-ES' 'a'
pico2wave -w=b.wav -l='es-ES' 'b'
pico2wave -w=c.wav -l='es-ES' 'c'
pico2wave -w=d.wav -l='es-ES' 'd'
pico2wave -w=e.wav -l='es-ES' 'e'
pico2wave -w=f.wav -l='es-ES' 'f'
pico2wave -w=g.wav -l='es-ES' 'g'
pico2wave -w=h.wav -l='es-ES' 'h'
pico2wave -w=i.wav -l='es-ES' 'i'
pico2wave -w=j.wav -l='es-ES' 'j'
pico2wave -w=k.wav -l='es-ES' 'k'
pico2wave -w=l.wav -l='es-ES' 'l'
pico2wave -w=m.wav -l='es-ES' 'm'
pico2wave -w=n.wav -l='es-ES' 'n'
pico2wave -w=o.wav -l='es-ES' 'o'
pico2wave -w=p.wav -l='es-ES' 'p'
pico2wave -w=q.wav -l='es-ES' 'q'
pico2wave -w=r.wav -l='es-ES' 'r'
pico2wave -w=s.wav -l='es-ES' 's'
pico2wave -w=t.wav -l='es-ES' 't'
pico2wave -w=u.wav -l='es-ES' 'u'
pico2wave -w=v.wav -l='es-ES' 'v'
pico2wave -w=w.wav -l='es-ES' 'w'
pico2wave -w=x.wav -l='es-ES' 'x'
pico2wave -w=y.wav -l='es-ES' 'y'
pico2wave -w=z.wav -l='es-ES' 'z'