//Ejercicio 6: Sumar una serie de n�meros hasta que se ingrese un negativo
//Descripci�n: Este programa suma una serie de n�meros ingresados por el usuario hasta que se ingrese un n�mero negativo, momento en el cual termina el bucle.
Algoritmo SumarHastaNegativo
	Definir numero, suma Como Real
    suma = 0
	
    // Bucle para sumar n�meros hasta que se ingrese un negativo
    Repetir
        Escribir "Ingrese un n�mero (negativo para terminar): "
        Leer numero
        Si numero >= 0 Entonces
            suma = suma + numero
        FinSi
    Hasta Que numero < 0
	
    // Mostrar el resultado de la suma
    Escribir "La suma de los n�meros ingresados es: ", suma
FinAlgoritmo
