// El programa solicita al usuario ingresar n�meros y los suma. El proceso contin�a hasta que el usuario ingrese un n�mero negativo.
Algoritmo LeerHastaNegativo
	Definir numero, suma Como Entero
    suma = 0
	
    // Bucle while para leer n�meros hasta que se ingrese un negativo
    Escribir "Ingrese un n�mero (negativo para terminar): "
    Leer numero
    Mientras numero >= 0 Hacer
        suma = suma + numero
        Escribir "Ingrese otro n�mero (negativo para terminar): "
        Leer numero
    FinMientras
	
    // Mostrar el resultado de la suma
    Escribir "La suma de los n�meros ingresados es: ", suma
FinAlgoritmo
