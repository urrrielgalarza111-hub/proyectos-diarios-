#Confeccionar una función que reciba tres enteros y
# nos muestre el mayor de ellos.
# La carga de los valores hacerlo por teclado

def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es: ")
    if v1>v2 and v1>v2:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)
            
            
def cargar():
    val1=int(input("Ingrese el primer valor: "))
    val2=int(input("Ingrese el segundo valor: "))
    val3=int(input("Ingrese el tercer valor: "))
    mostrar_mayor(val1,val2,val3)
    
    
#programa principal

cargar()