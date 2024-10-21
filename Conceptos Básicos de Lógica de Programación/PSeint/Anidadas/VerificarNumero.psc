Algoritmo VerificarNumero
    // Este algoritmo determina si un número es positivo, negativo o cero.
    
    Definir numero Como Real
    
    // Leer el número del usuario
    Escribir "Introduce un número:"
    Leer numero
    
    // Verificar si el número es positivo, negativo o cero utilizando condiciones múltiples
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
