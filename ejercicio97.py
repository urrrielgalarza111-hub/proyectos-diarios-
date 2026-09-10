#Confeccionar una función que calcule la
# superficie de un rectángulo y la retorne,
# la función recibe como parámetros los valores de dos de sus lados:
#def retornar_superficie(lado1,lado2):

def retornar_superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie


#bloque principal

print("Primer rectangulo")
lado1=int(input("Ingrese lado menor del rectangulo:"))
lado2=int(input("Ingrese lado mayor del rectangulo:"))
print("Segundo rectangulo")
lado3=int(input("Ingrese lado menor del rectangulo:"))
lado4=int(input("Ingrese lado mayor del rectangulo:"))
if retornar_superficie(lado1,lado2)==retornar_superficie(lado3,lado4):
    print("los dos rectangulos tienen la misma superficie")
else:
    if retornar_superficie(lado1,lado2)>retornar_superficie(lado3,lado4):
        print("El primer rectangulo tiene mas superficie que el segundo")
    else:
        print("El segundo rectangulo tiene mas superficie que el primero")