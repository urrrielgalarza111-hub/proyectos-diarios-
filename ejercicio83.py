#Desarrollar un programa con dos funciones.
# La primer solicite el ingreso de un entero
# y muestre el cuadrado de dicho valor.
# La segunda que solicite la carga de dos valores
# y muestre el producto de los mismos.
# LLamar desde el bloque del programa principal a ambas funciones

def ingreso_entero():
    valor=int(input("Ingrese un valor: "))
    cuadrado=valor**2
    print(cuadrado)
    print("***********")
    
def producto_dos_valores():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    producto=valor1*valor2
    print(producto)
    
#Bloque principal

ingreso_entero()
producto_dos_valores()