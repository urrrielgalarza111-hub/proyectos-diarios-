#Realizar la carga de dos nombres por teclado.
# Mostrar cual de los dos es mayor alfabéticamente o si son iguales

nom1=input("Ingrese el primer nombre: ")
nom2=input("Ingrese el segundo nombre: ")

if nom1>nom2:
    print(nom1)
else:
    if nom2>nom1:
        print(nom2)
    else:
        print("Los nombres son iguales")