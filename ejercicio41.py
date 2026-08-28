#Codificar un programa que lea n números enteros y calcule la
# cantidad de valores mayores o iguales a 1000 (n se carga por teclado)

mayorigual1000=0
n=int(input("Ingrese la cantidad de valores a evaluar: "))

for x in range(n):
    num=int(input("Ingrese valor: "))
    if num>=1000:
        mayorigual1000=mayorigual1000+1
        
    