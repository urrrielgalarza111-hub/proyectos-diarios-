#Definir una lista vacía y luego solicitar la carga de 5 enteros
# por teclado y añadirlos a la lista. Imprimir la lista generada.

lista=[]

while len(lista)<5:
    num=int(input("Ingrese un numero entero: "))
    lista.append(num)
    
print("La lista generada es: ", lista)