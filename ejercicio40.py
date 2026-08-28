#Escribir un programa que lea 10 números enteros y 
# luego muestre cuántos valores ingresados fueron múltiplos de 3 y
# cuántos de 5.
# Debemos tener en cuenta que hay números que son múltiplos de 3 y
# de 5 a la vez.
mult3=0
mult5=0
for x in range(11):
    num=int(input("Ingrese un valor: "))
    if num%3==0:
        mult3=mult3+1
    else:
        mult5=mult5+1

print("Valores que son multiplos de 3: ")
print(mult3)
print("Valores que son multiplos de 5: ")
print(mult5)