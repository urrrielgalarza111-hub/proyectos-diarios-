#Ejercicio B2 — Máximo de tres números
#Definir una función maximo3(a, b, c) que devuelva el mayor de tres valores, usando comparaciones (if/elif/else y operadores lógicos), 
#sin usar la función predefinida max.
#Pista: a es el mayor si a >= b and a >= c. Probala con casos donde el mayor esté en cada posición, y con valores repetidos como maximo3(5, 5, 2).

def maximo3(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c 
    
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

print("El mayor de los tres numeros es: ", maximo3(num1, num2, num3))