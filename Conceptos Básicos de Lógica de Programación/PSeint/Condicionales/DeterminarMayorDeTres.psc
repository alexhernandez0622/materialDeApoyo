Algoritmo DeterminarMayorDeTres
	Definir numero1, numero2, numero3, mayor Como Entero
	
    // Solicitar al usuario que ingrese los tres n�meros
    Escribir "Ingrese el primer n�mero: "
    Leer numero1
    Escribir "Ingrese el segundo n�mero: "
    Leer numero2
    Escribir "Ingrese el tercer n�mero: "
    Leer numero3
	
    // Determinar el mayor de los tres n�meros
    mayor = numero1
    Si numero2 > mayor Entonces
        mayor = numero2
    FinSi
    Si numero3 > mayor Entonces
        mayor = numero3
    FinSi
	
    // Mostrar el n�mero mayor
    Escribir "El n�mero mayor es: ", mayor
FinAlgoritmo
