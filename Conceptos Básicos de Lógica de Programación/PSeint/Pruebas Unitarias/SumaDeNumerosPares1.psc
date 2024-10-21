Algoritmo SumaDeNumerosPares
	// Definición de variables
	Definir N, suma, i Como Entero
	
	// Inicialización de variables
	Escribir "Ingrese el valor de N:"
	Leer N
	suma <- 0
	i <- 1
	
	// Bucle para sumar los primeros N números pares
	Mientras i <= N Hacer
		// Error: No se está considerando solo números pares
		suma <- suma + i
		i <- i + 1
	FinMientras
	
	// Mostrar el resultado
FinAlgoritmo
