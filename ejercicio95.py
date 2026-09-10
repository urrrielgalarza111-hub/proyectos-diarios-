#Elaborar una función que reciba tres enteros
# y nos retorne el valor promedio de los mismos.

def carga_y_promedio(v1,v2,v3):
    prom=(v1+v2+v3)//3
    print("El promedio de los valores ",v1,v2,v3," es: ")
    print(prom)
    
#bloque principal

valor1=int(input("Ingrese el primer valor: "))  
valor2=int(input("Ingrese el segundo valor: "))
valor3=int(input("Ingrese el tercer valor: "))
carga_y_promedio(valor1,valor2,valor3)

