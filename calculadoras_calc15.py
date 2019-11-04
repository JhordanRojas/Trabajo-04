#velocidad angular de una particula que gira circularmente
velocidad_angular,velocidad_tangencial,longitu_arco,tiempo,radio=0.0,0.0,0.0,0.0,0.0

#asignacion de valores
longitu_arco=60
tiempo=5
radio=3

#calculos
velocidad_tangencial=(longitu_arco/tiempo)
velocidad_angular=(velocidad_tangencial/radio)

#mostrar resultados
print("el valor de la londitud de arco es:",longitu_arco)
print("el valor del tiempo es:",tiempo,"s")
print("el valor de la velocidad tangencial es:",velocidad_tangencial,"m/s")

print("el valor de la velocidadangular de la particula es:",velocidad_angular,"rad/s")
