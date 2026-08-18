#Ejercicio A1 — Número positivo, negativo o cero  ★
#Escribir un programa que pida un número flotante y muestre si es positivo, negativo o cero. Usar if / elif / else.
#Salida esperada (ejemplos): con -3.5 → "El número es negativo."; con 0 → "El número es cero."

num=float(input("Ingrese un número flotante: "))

if num > 0:
    print(num, "El número es positivo ")
elif num < 0:
    print(num, "El número es negativo ")
else:
    print(num, "El número es cero ")
