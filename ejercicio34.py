#Desarrollar un programa que permita cargar n números enteros y 
# luego nos informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional 
# (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
#	if valor%2==0:         

i=1
contpar=0
contimpar=0
n=int(input("ingrese la cantida de numeros que queiras procesar: "))
while i<=n:
    valor = int(input("ingese un valor: "))
    i=i+1
    
    if valor%2==0:
        contpar=contpar+1
    else:
        contimpar=contimpar+1
        
print("Cantidad de valores par: ")
print(contpar)
print("Cantidad de valores impar: ")
print(contimpar)