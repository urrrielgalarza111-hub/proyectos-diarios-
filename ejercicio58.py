#Definir una lista que almacene por asignación los nombres de 5 personas.
# Contar cuantos de esos nombres tienen 5 o más caracteres.

nombres=["Uriel","Juan","Pedro","Maria","Ana"]
contador=0
for x in range(len(nombres)):
    if len(nombres[x])>=5:
        contador=contador+1
        print("El nombre ", nombres[x], " tiene 5 o más caracteres")
        
print("La cantidad de nombres con 5 o más caracteres es: ", contador)
