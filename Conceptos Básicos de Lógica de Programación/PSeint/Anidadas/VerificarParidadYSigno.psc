Algoritmo VerificarParidadYSigno
	// Este algoritmo determina si un n�mero es par o impar, y si es positivo o negativo.
    
    Definir numero Como Entero
    
    // Leer el n�mero del usuario
    Escribir "Introduce un n�mero entero:"
    Leer numero
    
    // Verificar paridad utilizando condiciones anidadas
    Si numero MOD 2 = 0 Entonces
        Escribir "El n�mero es par."
        Si numero > 0 Entonces
            Escribir "El n�mero es positivo."
        Sino
            Escribir "El n�mero es negativo o cero."
        FinSi
    Sino
        Escribir "El n�mero es impar."
        Si numero > 0 Entonces
            Escribir "El n�mero es positivo."
        Sino
            Escribir "El n�mero es negativo."
        FinSi
    FinSi
FinAlgoritmo

