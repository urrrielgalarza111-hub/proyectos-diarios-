#Realizar la carga de valores enteros por teclado,
# almacenarlos en una lista.
# Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el
# tamaño de la lista.

lista=[]

print("Ingrese valores enteros. Para finalizar ingrese 0.")

while True:
    num=int(input("Ingrese un numero entero: "))
    if num==0:
        break
    lista.append(num)
    
print("La cantidad de numeros ingresados es: ", len(lista))
print("La lista generada es: ", lista)