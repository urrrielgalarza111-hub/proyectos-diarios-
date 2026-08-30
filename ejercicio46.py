#Realizar un programa que lea los lados de n triángulos, e informar:
#a) De cada uno de ellos, qué tipo de triángulo es:
# equilátero (tres lados iguales), isósceles (dos lados iguales),
# o escaleno (ningún lado igual)
#b) Cantidad de triángulos de cada tipo.

equi=0
isose=0
escal=0

n=int(input("Ingrese la cantidad de trangulos a procesar: "))
lA=0
lB=0
lC=0
for x in range(n):
    lA=int(input("Ingrese el valor del lado A: "))
    lB=int(input("Ingrese el valor del lado B: "))
    lC=int(input("Ingrese el valor del lado C: "))
    
    if lA == lB and lA == lC:
        print("Es equilatero")
        equi=equi+1
    else:
        if lA == lB or lA == lC or lB == lC:
            print("Es isosceles")
            isose=isose+1
        else:
            print("Es escaleno")
            escal=escal+1
            
print("equilatero: ")
print(equi)
print("isosceles: ")
print(isose)
print("escaleno: ")
print(escal)