#Ejercicio B8 — Funciones predefinidas
#Pedir tres números enteros y mostrar:
#1. El mayor usando max. 
#2. El menor usando min.
#3. La diferencia absoluta entre mayor y menor usando abs.
#4. La cantidad de dígitos del número mayor usando len y str compuestas: len(str(mayor)).

def numero_max(n1,n2,n3):
   return max(n1,n2,n3)


def numero_min(n1,n2,n3):
   return min(n1,n2,n3)
    
    
def dif_absoluta(mayor,menor):
    return abs(mayor-menor)

def cant_digitos(numero):
    return len(str(numero))


#bloque principal
num1=(int(input("Ingrese el primer numero: ")))
num2=(int(input("Ingrese el segundo numero: ")))
num3=(int(input("Ingrese el tercer numero: ")))

mayor=numero_max(num1,num2,num3)
menor=numero_min(num1,num2,num3)
diferencia=dif_absoluta(mayor,menor)
cantidad=cant_digitos(mayor)

print("1. El numero mayor es:", mayor)
print("2. El numero menor es:", menor)
print("3. La diferencia absoluta entre el mayor y el menor es de:", diferencia)
print("4. La cantidad de digitos del numero mayor es:", cant_digitos)