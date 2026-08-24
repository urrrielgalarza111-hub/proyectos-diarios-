#Problema 4:
#Una planta que fabrica perfiles de hierro posee un lote de n piezas.
#Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil;
#sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas.
#Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

cantpiezas=int(input("ingresar la cantidad de piezasa progresar:"))
aptas=0
i=1

while i<= cantpiezas:
    
    longitud=float(input("ingresar la longitud de las piezas: "))
    if longitud>=1.20 and longitud<=1.30:
        aptas=aptas+1
    i=i+1

print("la cantidad de piezas aptas es: ", aptas)