#Mapeo de Píxeles: Calcular el área total y el perímetro de un mapa 2D compuesto por baldosas (tiles). 
# Pedir al usuario la cantidad de filas y columnas, asumiendo que cada baldosa tiene un lado constante de 32 píxeles
filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas: "))

#Calcular el area total y el perimetro del mapa
area_total=filas*columnas*32*32
perimetro=2*(filas*32 + columnas*32)

#Mostrar los resultados al al asuario
print("El área total del mapa es:", area_total, "píxeles cuadrados")
print("El perímetro del mapa es:", perimetro, "píxeles")