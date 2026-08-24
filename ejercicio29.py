#Se ingresan un conjunto de n alturas de personas por teclado.
# Mostrar la altura promedio de las personas.

promedio=0
suma=0
i=1
cantpersonas=int(input("ingresar la cantidad de personas: "))
while i<=cantpersonas:
    altura=float(input("ingresar la altura de la persona: "))
    suma=suma+altura
    i=i+1
    
promedio=suma/cantpersonas

print("la altura promedio de las personas es: ", promedio)