Algoritmo VerificarNumero
    // Este algoritmo determina si un n�mero es positivo, negativo o cero.
    
    Definir numero Como Real
    
    // Leer el n�mero del usuario
    Escribir "Introduce un n�mero:"
    Leer numero
    
    // Verificar si el n�mero es positivo, negativo o cero utilizando condiciones m�ltiples
    Si numero > 0 Entonces
        Escribir "El n�mero es positivo."
    Sino
        Si numero < 0 Entonces
            Escribir "El n�mero es negativo."
        Sino
            Escribir "El n�mero es cero."
        FinSi
    FinSi
FinAlgoritmo
