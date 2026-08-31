#Realizar la carga por teclado del nombre,
# edad y altura de dos personas.
# Mostrar por pantalla el nombre de la persona con mayor altura.

print("Primera persona ")
nom1=input("Ingrese el primer nombre: ")
edad1=int(input("Ingrese la primera edad: "))
alt1=float(input("Ingrese la primera altura: "))

print("Segunda persona ")
nom2=input("Ingrese el segundo nombre: ")
edad2=int(input("Ingrese la segunda edad: "))
alt2=float(input("Ingrese la segunda altura: "))

if alt1 > alt2:
    print(nom1)
    print(edad1)
    print(alt1)
else:
    print(nom2)
    print(edad2)
    print(alt2)