#Desarrollar un programa que solicite la carga
# de tres valores y muestre el menor.
# Desde el bloque principal del programa llamar 
# 2 veces a dicha función (sin utilizar una estructura repetitiva)

def carga_tres_valores():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    valor3=int(input("Ingrese el tercer valor: "))
    if valor1<=valor2 and valor1<=valor3:
        print(valor1)
    elif valor2<=valor1 and valor2<=valor3:
        print(valor2)
    else:
        print(valor3)
        
#bloque principal

carga_tres_valores()
carga_tres_valores()
