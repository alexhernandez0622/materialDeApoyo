Algoritmo ClasificarEdad
    // Este algoritmo clasifica a una persona como ni�o, adolescente, adulto o anciano seg�n su edad.
    
    Definir edad Como Entero
    
    // Leer la edad de la persona
    Escribir "Introduce la edad de la persona:"
    Leer edad
    
    // Clasificar la edad utilizando condiciones anidadas
    Si edad >= 0 Y edad <= 12 Entonces
        Escribir "Ni�o"
    Sino
        Si edad >= 13 Y edad <= 17 Entonces
            Escribir "Adolescente"
        Sino
            Si edad >= 18 Y edad <= 64 Entonces
                Escribir "Adulto"
            Sino
                Si edad >= 65 Entonces
                    Escribir "Anciano"
                FinSi
            FinSi
        FinSi
    FinSi
FinAlgoritmo
