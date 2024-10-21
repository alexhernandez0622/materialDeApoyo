Algoritmo diccionario_y_tuplas
    Definir ventas Como Real[3][2]
    Definir total Como Real
    Definir producto Como Caracter
    Definir cantidad, precio_unitario Como Real
	
    // Crear un diccionario (en PSeInt se simula con una lista de registros)
    ventas["ProductoA"] <- Real[10, 150]
    ventas["ProductoB"] <- Real[5, 300]
    ventas["ProductoC"] <- Real[12, 50]
	
    // Calcular y mostrar el total de ventas por producto
    Para Cada producto En ventas Hacer
        cantidad <- ventas[producto][1]
        precio_unitario <- ventas[producto][2]
        total <- cantidad * precio_unitario
        Escribir "Total ventas para ", producto, ": ", total
    FinPara
FinAlgoritmo
