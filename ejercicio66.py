#Ingresar por teclado los nombres
# de 5 personas y almacenarlos en una lista.
# Mostrar el nombre de persona menor en orden alfabético.

lista=[]
for x in range(5):
    nom=input("Ingrese un nombre: ")
    lista.append(nom)

nombremen=lista[0]
for x in range(5):
    if lista[x]<nombremen:
        nombremen=lista[x]
        
print("El nombre menor en orden alfabético es: ", nombremen)
