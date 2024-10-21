//Ejercicio 6: Sumar una serie de números hasta que se ingrese un negativo
//Descripción: Este programa suma una serie de números ingresados por el usuario hasta que se ingrese un número negativo, momento en el cual termina el bucle.
Algoritmo SumarHastaNegativo
	Definir numero, suma Como Real
    suma = 0
	
    // Bucle para sumar números hasta que se ingrese un negativo
    Repetir
        Escribir "Ingrese un número (negativo para terminar): "
        Leer numero
        Si numero >= 0 Entonces
            suma = suma + numero
        FinSi
    Hasta Que numero < 0
	
    // Mostrar el resultado de la suma
    Escribir "La suma de los números ingresados es: ", suma
FinAlgoritmo
