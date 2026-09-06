#Desarrollar un programa que permita ingresar el lado de un cuadrado. 
# Luego preguntar 
# si quiere calcular y mostrar su perímetro o su superficie.

def mostrar_perimetro(lado):
    per=lado*4
    print("La superficie es ", per)
    
def mostar_superficie(lado):
    sup=lado*lado
    print("La superficiees es ",sup)
    
def cargar_dato():
    la=int(input("Ingrese el valor del lado de un cuadrado: "))
    respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]?: ")
    if respuesta=="perimetro":
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostar_superficie(la)
        
#programa principal

cargar_dato()