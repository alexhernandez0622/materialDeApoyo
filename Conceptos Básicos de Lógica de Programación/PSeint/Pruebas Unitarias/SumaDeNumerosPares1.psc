Algoritmo SumaDeNumerosPares
	// Definici�n de variables
	Definir N, suma, i Como Entero
	
	// Inicializaci�n de variables
	Escribir "Ingrese el valor de N:"
	Leer N
	suma <- 0
	i <- 1
	
	// Bucle para sumar los primeros N n�meros pares
	Mientras i <= N Hacer
		// Error: No se est� considerando solo n�meros pares
		suma <- suma + i
		i <- i + 1
	FinMientras
	
	// Mostrar el resultado
FinAlgoritmo
