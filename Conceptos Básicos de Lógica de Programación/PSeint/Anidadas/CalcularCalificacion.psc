Algoritmo CalcularCalificacion
    // Este algoritmo asigna una calificaci�n basada en el promedio de un estudiante.
    
    Definir promedio Como Real
    
    // Leer el promedio del estudiante
    Escribir "Introduce el promedio del estudiante:"
    Leer promedio
    
    // Determinar la calificaci�n utilizando condiciones anidadas
    Si promedio >= 90 Entonces
        Escribir "Calificaci�n: Excelente"
    Sino
        Si promedio >= 80 Entonces
            Escribir "Calificaci�n: Sobresaliente"
        Sino
            Si promedio >= 70 Entonces
                Escribir "Calificaci�n: Aceptable"
            Sino
                Si promedio >= 60 Entonces
                    Escribir "Calificaci�n: Insuficiente"
                Sino
                    Escribir "Calificaci�n: Deficiente"
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo
