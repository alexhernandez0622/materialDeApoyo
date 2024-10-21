// El programa solicita al usuario ingresar números y los suma. El proceso continúa hasta que el usuario ingrese un número negativo.
Algoritmo LeerHastaNegativo
	Definir numero, suma Como Entero
    suma = 0
	
    // Bucle while para leer números hasta que se ingrese un negativo
    Escribir "Ingrese un número (negativo para terminar): "
    Leer numero
    Mientras numero >= 0 Hacer
        suma = suma + numero
        Escribir "Ingrese otro número (negativo para terminar): "
        Leer numero
    FinMientras
	
    // Mostrar el resultado de la suma
    Escribir "La suma de los números ingresados es: ", suma
FinAlgoritmo
