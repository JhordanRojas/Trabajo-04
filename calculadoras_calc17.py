#calculo del tiempo de encuentro de dos autos en direcciones opuestas
tiempo_encuentro,distancia,vel1,vel2=0.0,0.0,0.0,0.0

#asignacion de valores
distancia=120
vel1=35
vel2=28

#calculos
tiempo_encuentro=(distancia/(vel2+vel1))

#mostrar resultados
print("el valor de la distancia es:",distancia,"m")
print("el valor de la velocidad del primer auto es:",vel1,"m/s")
print("el valor de la velocidad del segundo auto es:",vel2,"m/s")

print("el valor del tiempo de encuentro de los autos es:",tiempo_encuentro,"s")
