#Potencia de un motor de ascensor al levantar una cabina
potencia,fuerza,velocidad,masa,aceleracion=0.0,0.0,0.0,0.0,0.0

#asignacion de valores
masa=520
aceleracion=16
velocidad=35

#calculos
fuerza=(masa*aceleracion)
potencia=(fuerza*velocidad)

#mostrar valores
print("el valor de la masa es:",masa,"kg")
print("el valor de la aceleracion es:",aceleracion,"m/s")
print("el valor de la fuerza es:",fuerza,"N")

print("el valor de la potencia instantanea es:",potencia,"J/s")
