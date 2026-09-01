#Realizar la carga de enteros por teclado. 
# Preguntar después que ingresa el valor si desea
# cargar otro valor debiendo el operador ingresar la cadena
# 'si' o 'no' por teclado.
#Mostrar la suma de los valores ingresados.

num=int(input("Ingrese un numero: "))
suma=num
resp=input("desea ingresar otro numero? (si/no): ")
while resp=="si":
    num=int(input("Ingrese otro numero: "))
    suma+=num
    resp=input("desea ingresar otro numero? (si/no): ")
print("La suma de los numeros ingresados es:", suma)