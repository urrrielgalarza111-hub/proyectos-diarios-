#Confeccionar un programa que permita ingresar un valor 
# del 1 al 10 y nos muestre la tabla de multiplicar del mismo 
# (los primeros 12 términos)
#Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 
# 3, 6, 9, hasta el 36.

n=int(input("Ingrese un numero el cual quiere ver su tabla de multiplicar: "))
num=0
for x in range(12):
    print(num+n)
    num=num+n
     