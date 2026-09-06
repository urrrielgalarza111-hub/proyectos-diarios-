#Confeccionar una función que reciba tres
# enteros y nos muestre el mayor de ellos.
# La carga de los valores hacerlo por teclado.

def valor_mayor_de_tres(v1,v2,v3):
    print("El valor mayor de los tres numeros es: ")
    if v1>=v2 and v1>=v3:
        print(v1)
    elif v2>=v1 and v2>=v3:
        print(v2)
    else:
        print(v3)
        
def cargar():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    valor3=int(input("Ingrese el tercer valor: "))
    valor_mayor_de_tres(valor1,valor2,valor3)
    
#programa principal

cargar()