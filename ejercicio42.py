#Confeccionar un programa que lea n pares de datos,
# cada par de datos corresponde a la medida de la base y 
# la altura de un triángulo. El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.

mayor12=0
n=int(input("Ingrese la cantidad de datos pares: "))
for x in range(n):
    base=int(input("Ingrese el valor de la base: "))
    altura=int(input("Ingrese el valor de la altura: "))
    superficie=(base+altura)/2
    if superficie>12:
       mayor12=mayor12+1
        
    print("base: ")
    print(base)
    print("altura: ")
    print(altura)
    print("superficie: ")
    print(superficie)
    
print("La cantidad de superficies mayores a 12: ")
print(mayor12)
    