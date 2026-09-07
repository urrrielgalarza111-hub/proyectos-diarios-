#Elaborar una función que reciba tres enteros
# y nos retorne el valor promedio de los mismos.

def retornar_promedio(v1,v2,v3):
    promedio=(v1+v2+v3)//3
    return promedio

#bloque princial

val1=int(input("Ingrese el primer valor: "))
val2=int(input("Ingrese el segundo valor: "))
val3=int(input("Ingrese el tercer valor: "))

print("valor promedio de los tres numeros",retornar_promedio(val1,val2,val3))

