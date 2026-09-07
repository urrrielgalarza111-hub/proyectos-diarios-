#Confeccionar una función que le enviemos como parámetro
# un string y nos retorne la cantidad de caracteres que tiene.
# En el bloque principal solicitar la carga de 
# dos nombres por teclado y llamar a la función dos veces. Imprimir 
# en el bloque principal cual de las dos palabras tiene más caracteres.

def largo(cadena):
    return len(cadena)

nom1=input("Ingrese el primer nombre: ")
nom2=input("Ingrese el segundo nombre: ")
la1=largo=(nom1)
la2=largo=(nom2)

if la1==la2:
    print("Los nombres: ",nom1,nom2,"tienen la misma cantidad de caracteres")
else:
    if la1>la2:
        print(nom1,"es mas largo")
    else:
        print(nom2,"es mas largo")