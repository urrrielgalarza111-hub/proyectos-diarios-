#Desarrollar un programa que solicite la carga de 10 números
# e imprima la suma de los últimos 5 valores ingresados.

print("Ingrese 10 numenos: ")
suma=0
for x in range(10):
    num=int(input("Ingrese un valor: "))
    if x >=5:
        suma=suma+num
        
print("la suma de los ultimo 5 numeros es: ")
print(suma)