// solicita tres n�meros y llama a otro procedimiento para determinar el mayor de ellos.
Funcion MostrarMayor(num1, num2, num3)
    Definir mayor Como Real
	
    // Determinar el mayor n�mero
    mayor = num1
    Si num2 > mayor Entonces
        mayor = num2
    FinSi
    Si num3 > mayor Entonces
        mayor = num3
    FinSi
	
    // Mostrar el mayor n�mero
    Escribir "El n�mero mayor es: ", mayor
FinFuncion
	
Algoritmo  EncontrarMayorDeTresNumeros
	
    Definir numero1, numero2, numero3 Como Real
	
    // Solicitar los tres n�meros al usuario
    Escribir "Ingrese el primer n�mero: "
    Leer numero1
    Escribir "Ingrese el segundo n�mero: "
    Leer numero2
    Escribir "Ingrese el tercer n�mero: "
    Leer numero3
	
    // Llamar al procedimiento para determinar el mayor n�mero
    MostrarMayor(numero1, numero2, numero3)
	
FinAlgoritmo
