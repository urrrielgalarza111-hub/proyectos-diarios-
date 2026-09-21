#Ejercicio A1 — Número positivo, negativo o cero  ★
#Escribir un programa que pida un número flotante
#y muestre si es positivo, negativo o cero. Usar if / elif / else.
#Salida esperada (ejemplos): con -3.5 → "El número es negativo.";
#con 0 → "El número es cero."
#Recordá: input() siempre devuelve una cadena (str): convertí 
#con float() antes de comparar con números.

num=float(input("Ingrese un numero real "))

if num>0:
    print(num," es positivo")
else:
    if num<0:
        print(num," es negativo")
    else:
        print(num," es cero")