Algoritmo MayorDeTresNumeros
	// Declaración de variables
    Definir num1, num2, num3, mayor Como Real
    
    // Solicitar al usuario el primer número
    Escribir "Ingrese el primer número:"
    Leer num1
    
    // Solicitar al usuario el segundo número
    Escribir "Ingrese el segundo número:"
    Leer num2
    
    // Solicitar al usuario el tercer número
    Escribir "Ingrese el tercer número:"
    Leer num3
    
    // Inicializar la variable mayor con el primer número
    mayor <- num1
    
    // Comparar el segundo número con el mayor actual
    Si num2 > mayor Entonces
        mayor <- num2
    FinSi
    
    // Comparar el tercer número con el mayor actual
    Si num3 > mayor Entonces
        mayor <- num3
    FinSi
    
    // Mostrar el mayor de los tres números
    Escribir "El mayor de los tres números es: ", mayor
FinAlgoritmo
