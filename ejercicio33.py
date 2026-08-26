#Realizar un programa que permita cargar dos listas de 15 valores cada una.
# Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

suma1=0
suma2=0
i=1
print("primera lista: ")
while i<=15:
    valor=int(input("Ingrese un valor: "))
    suma1=suma1+valor
    i=i+1
i=1
print("segunda lista: ")
while i<=15:
    valor=int(input("Ingrese un valor: "))
    suma2=suma2+valor
    i=i+1
    
if suma1 > suma2:
    print("lista 1 es mayor que lista 2")
else:
    if suma2>suma1:
        print("lista 2 es mayor que lista 1")
    else:
       print("las 2 listas son iguales")