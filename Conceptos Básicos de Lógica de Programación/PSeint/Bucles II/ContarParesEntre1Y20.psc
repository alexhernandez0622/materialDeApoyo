// Programa: Adivina el Número en PSeInt
// Descripción: El programa genera un número aleatorio entre 1 y 10 utilizando un subproceso.
//              El usuario tiene que adivinar el número. El programa dará pistas si el número es demasiado bajo o alto.
Proceso AdivinarNumero
    Definir numeroSecreto, intento Como Entero
    Definir adivinado Como Logico
    
    // Generamos un número secreto aleatorio entre 1 y 10
    numeroSecreto = Aleatorio(1, 10)
    
    // Inicializamos la variable que controla si se ha adivinado el número
    adivinado = Falso
    
    // Repetimos el proceso hasta que el número sea adivinado
    Mientras adivinado = Falso Hacer
        // Solicitamos al usuario que adivine el número
        Escribir "Adivina un número entre 1 y 10: "
        Leer intento
        
        // Verificamos si el intento es igual al número secreto
        Si intento = numeroSecreto Entonces
            // Si es correcto, mostramos un mensaje y terminamos el bucle
            Escribir "¡Felicidades! Adivinaste el número."
            adivinado = Verdadero
        Sino
            // Si es incorrecto, mostramos un mensaje de error
            Escribir "Ese no es el número correcto. Inténtalo de nuevo."
        FinSi
    FinMientras
FinProceso


