#dilatacion de una barra de hierro
dilatacion,longitud_inicial,variacion_temperatura,coef_dilatacion=0.0,0.0,0.0,0.0

#asignacion de valores
longitud_inicial=12
variacion_temperatura=64
coef_dilatacion=0.0018

#calculos
dilatacion=(longitud_inicial*variacion_temperatura*coef_dilatacion)

#mostrar resultados
print("el valor de la longitud de la varilla es:",longitud_inicial)
print("el valor de la variacion de la temperatura es:",variacion_temperatura)
print("el valor del coeficiente de dilatacion es:",coef_dilatacion)

print("la dilatacion de la varilla es de:",dilatacion)
