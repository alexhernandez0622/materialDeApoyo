Algoritmo CalcularCalificacion
    // Este algoritmo asigna una calificación basada en el promedio de un estudiante.
    
    Definir promedio Como Real
    
    // Leer el promedio del estudiante
    Escribir "Introduce el promedio del estudiante:"
    Leer promedio
    
    // Determinar la calificación utilizando condiciones anidadas
    Si promedio >= 90 Entonces
        Escribir "Calificación: Excelente"
    Sino
        Si promedio >= 80 Entonces
            Escribir "Calificación: Sobresaliente"
        Sino
            Si promedio >= 70 Entonces
                Escribir "Calificación: Aceptable"
            Sino
                Si promedio >= 60 Entonces
                    Escribir "Calificación: Insuficiente"
                Sino
                    Escribir "Calificación: Deficiente"
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo
