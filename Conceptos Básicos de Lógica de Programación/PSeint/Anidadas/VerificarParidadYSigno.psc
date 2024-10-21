Algoritmo VerificarParidadYSigno
	// Este algoritmo determina si un número es par o impar, y si es positivo o negativo.
    
    Definir numero Como Entero
    
    // Leer el número del usuario
    Escribir "Introduce un número entero:"
    Leer numero
    
    // Verificar paridad utilizando condiciones anidadas
    Si numero MOD 2 = 0 Entonces
        Escribir "El número es par."
        Si numero > 0 Entonces
            Escribir "El número es positivo."
        Sino
            Escribir "El número es negativo o cero."
        FinSi
    Sino
        Escribir "El número es impar."
        Si numero > 0 Entonces
            Escribir "El número es positivo."
        Sino
            Escribir "El número es negativo."
        FinSi
    FinSi
FinAlgoritmo

