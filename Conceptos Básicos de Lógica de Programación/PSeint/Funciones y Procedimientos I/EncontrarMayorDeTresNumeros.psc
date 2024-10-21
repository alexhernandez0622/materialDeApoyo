// solicita tres números y llama a otro procedimiento para determinar el mayor de ellos.
Funcion MostrarMayor(num1, num2, num3)
    Definir mayor Como Real
	
    // Determinar el mayor número
    mayor = num1
    Si num2 > mayor Entonces
        mayor = num2
    FinSi
    Si num3 > mayor Entonces
        mayor = num3
    FinSi
	
    // Mostrar el mayor número
    Escribir "El número mayor es: ", mayor
FinFuncion
	
Algoritmo  EncontrarMayorDeTresNumeros
	
    Definir numero1, numero2, numero3 Como Real
	
    // Solicitar los tres números al usuario
    Escribir "Ingrese el primer número: "
    Leer numero1
    Escribir "Ingrese el segundo número: "
    Leer numero2
    Escribir "Ingrese el tercer número: "
    Leer numero3
	
    // Llamar al procedimiento para determinar el mayor número
    MostrarMayor(numero1, numero2, numero3)
	
FinAlgoritmo
