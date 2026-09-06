#Confeccionar una función que reciba el nombre de un operario, 
# el pago por hora y la cantidad de horas trabajadas.
# Debe mostrar su sueldo y el nombre.
# Hacer la llamada de la función mediante argumentos nombrados.

def calcular_sueldo(nombre, costohora, canthoras):
    sueldo=costohora*costohora
    print(nombre," trabajo: ",canthoras," horas y cobra: ", sueldo)
    
#bloque principal

calcular_sueldo("anna",100,450)
calcular_sueldo("jose",100,200)