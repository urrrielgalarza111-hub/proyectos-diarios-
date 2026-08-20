#Ejercicio B8 — Funciones predefinidas
#Pedir tres números enteros y mostrar:
#1. El mayor usando max.  
#2. El menor usando min.
#3. La diferencia absoluta entre mayor y menor usando abs.
#4. La cantidad de dígitos del número mayor usando len y str compuestas: len(str(mayor)).

num1=int(input("Ingrese el primer numero entero: "))
num2=int(input("Ingrese el segundo numero entero: "))
num3=int(input("Ingrese el tercer numero entero: "))

mayor=max(num1, num2, num3)
menor=min(num1, num2, num3)
diferencia=abs(mayor-menor)
digitos_mayor=len(str(mayor))
print("El mayor es: ", mayor)
print("El menor es:", menor)
print("La diferencia absoluta entre mayor y menor es: ", diferencia)
print("La cantidad de digitos del numero mayor es: ", digitos_mayor)
