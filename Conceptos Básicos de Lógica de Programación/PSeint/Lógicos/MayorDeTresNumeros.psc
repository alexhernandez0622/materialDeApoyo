Algoritmo MayorDeTresNumeros
	// Declaraci�n de variables
    Definir num1, num2, num3, mayor Como Real
    
    // Solicitar al usuario el primer n�mero
    Escribir "Ingrese el primer n�mero:"
    Leer num1
    
    // Solicitar al usuario el segundo n�mero
    Escribir "Ingrese el segundo n�mero:"
    Leer num2
    
    // Solicitar al usuario el tercer n�mero
    Escribir "Ingrese el tercer n�mero:"
    Leer num3
    
    // Inicializar la variable mayor con el primer n�mero
    mayor <- num1
    
    // Comparar el segundo n�mero con el mayor actual
    Si num2 > mayor Entonces
        mayor <- num2
    FinSi
    
    // Comparar el tercer n�mero con el mayor actual
    Si num3 > mayor Entonces
        mayor <- num3
    FinSi
    
    // Mostrar el mayor de los tres n�meros
    Escribir "El mayor de los tres n�meros es: ", mayor
FinAlgoritmo
