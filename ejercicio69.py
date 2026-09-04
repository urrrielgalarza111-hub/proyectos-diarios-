#Crear y cargar dos listas con los nombres
# de 5 productos en una y sus respectivos precios en otra. 
# Definir dos listas paralelas. Mostrar 
# cuantos productos tienen un precio mayor al primer producto ingresado.

productos=[]
precios=[]

for x in range(5):
    producto=input("Ingrese el nombre del producto: ")
    productos.append(producto)
    precio=float(input("Ingrese el precio del producto: "))
    precios.append(precio)
    
cantidad=0
for x in range(5):
 if precios[x]>precios[0]:
    cantidad=cantidad+1
    
print("La cantidad de productos con precio mayor al primer producto ingresado es: ",cantidad)   

            
            
    
    