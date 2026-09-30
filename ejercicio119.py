def validar_rango(mensaje,minimo,maximo):
    while True:
        opcion=int(input(mensaje))
        if  opcion>=minimo and opcion<=maximo:
            return opcion
        
def calcular_descuento_monto(subtotal):
    if subtotal>25000:
        return subtotal*0.10
    else:
        return subtotal*0.0
    
def calcular_ajuste_pago(monto,medio):
    match medio:
        case 1:
            return monto*0.05
        case 2:
            return monto*0.0
        case 3:
            return monto*0.08
        
def cuenta_regresiva(n):
    if n==0:
        print("!caja Cerrada!")
    else:
        print(n)
        return cuenta_regresiva(n-1)
    
#Contadores(enteros)
cant_ventas=0
cant_efectivo=0
cant_debito=0
cant_credito=0
#Acumuladores de dinero(flotantes)
recaudacion_total=0
total_bebidas=0.0
total_golosinas=0.0
total_almacen=0.0
total_libreria=0
#Venta maxima
venta_maxima=0.0

while True:
    print("---MENU PRINCIPAL---")
    print("1-Registrar venta")
    print("2-Resumen del dia")
    print("3-Cerrar caja")
    
    opcion=validar_rango("Elija una opcion(1-3):",1,2,3)
   
    match opcion:
        case 1:
            print("---REGISTRAR VENTAS---")
            catergoria=validar_rango("Seleccione categoría (1-Golosinas, 2-Bebidas, 3-Almacén, 4-Librería): ", 1, 4)
            