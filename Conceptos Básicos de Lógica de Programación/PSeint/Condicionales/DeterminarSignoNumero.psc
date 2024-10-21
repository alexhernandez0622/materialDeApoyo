Algoritmo DeterminarSignoNumero
	Definir numero Como Real
	
    // Solicitar al usuario ingresar un número
    Escribir "Ingrese un número: "
    Leer numero
	
    // Verificar si el número es positivo, negativo o cero
    Si numero > 0 Entonces
        Escribir "El número es positivo."
    Sino
        Si numero < 0 Entonces
            Escribir "El número es negativo."
        Sino
            Escribir "El número es cero."
        FinSi
    FinSi
FinAlgoritmo
