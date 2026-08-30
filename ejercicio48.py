#Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de múltiplos de 15.
#d) El valor acumulado de los números ingresados que son pares.

positivos=0
negativos=0
mult15=0
acumpar=0
num=0

for x in range(10):
    num=(input("Ingrese un valor: "))
    if num>0:
        positivos=positivos+1
    else:
        if num<0:
            negativos+negativos+1
        else:
            if num%15==0:
                mult15=mult15+1
            else:
                if num%2==0:
                    acumpar=acumpar+num
                    
print("valores positivos: ")
print(positivos)
print("valores negativos: ")
print(negativos)
print("valores multiplos de 15: ")
print(mult15)
print("valores pares acumulados: ")
print(acumpar)
                    
