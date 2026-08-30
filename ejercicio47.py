#Escribir un programa que pida ingresar coordenadas (x,y) 
# que representan puntos en el plano.
#Informar cuántos puntos se han ingresado en el primer,
# segundo, tercer y cuarto cuadrante.
# Al comenzar el programa se pide que se ingrese 
# la cantidad de puntos a procesar

I=0
II=0
III=0
IV=0
n=int(input("Ingresar cuntas cordenadas se va ingresar: "))

for i in range(n):
    x=int(input("Ingrese valor de la coordenada X: "))
    y=int(input("Ingrese valor de la coordenada Y: "))
    
    if x>0 and y>0:
        I=I+1
    else:
        if x<0 and y>0:
            II=II+1
        else:
            if x<0 and y<0:
                III=III+1
            else:
                IV=IV+1
                
print("sector I: ")
print(I)
print("sector II: ")
print(II)
print("sector III: ")
print(III)
print("sector IV: ")
print(IV)