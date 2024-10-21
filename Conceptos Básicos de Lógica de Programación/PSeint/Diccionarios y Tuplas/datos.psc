Algoritmo lista_y_tuplas
    Definir estudiantes Como Real[3][2]
    Definir nombre Como Caracter
    Definir nota Como Real
	
    // Crear una lista de tuplas
    estudiantes[1] <- Real["Ana", 8.5]
    estudiantes[2] <- Real["Luis", 9.0]
    estudiantes[3] <- Real["Carlos", 7.8]
	
    // Imprimir la lista de estudiantes y sus notas
    Para i <- 1 Hasta 3 Hacer
        nombre <- estudiantes[i][1]
        nota <- estudiantes[i][2]
        Escribir "Nombre: ", nombre, ", Nota: ", nota
    FinPara
FinAlgoritmo
