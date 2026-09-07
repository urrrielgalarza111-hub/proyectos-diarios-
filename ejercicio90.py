#Confeccionar una función que le enviemos como parámetro el valor 
# del lado de un cuadrado y nos retorne su superficie

def retornar_superficie(lado):
    sup=lado*lado
    return sup

#bloque principal

va=int(input("Ingrese un valor del lado del cuadrado: "))
superficie=retornar_superficie(va)
print("la superficie del cuadrado es: ",superficie)

