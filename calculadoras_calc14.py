#calcular el area de un pentagono regular
area_pentagono,apotema,perimetro,lado=0.0,0.0,0.0,0.0

#asignacion de valores
lado=8
apotema=12

#calculos
perimetro=(lado*5)
area_pentagono=((perimetro*apotema)/2)

#mostrar valores
print("el valor del lado del pentagono es:",lado,"cm")
print("el valor del apotema del pentagono es:",apotema,"cm")

print("el valor del ares del pentagono es:",area_pentagono,"cm cuadrados")
