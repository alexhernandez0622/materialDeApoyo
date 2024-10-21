// Programa: Adivina el N�mero en PSeInt
// Descripci�n: El programa genera un n�mero aleatorio entre 1 y 10 utilizando un subproceso.
//              El usuario tiene que adivinar el n�mero. El programa dar� pistas si el n�mero es demasiado bajo o alto.
Proceso AdivinarNumero
    Definir numeroSecreto, intento Como Entero
    Definir adivinado Como Logico
    
    // Generamos un n�mero secreto aleatorio entre 1 y 10
    numeroSecreto = Aleatorio(1, 10)
    
    // Inicializamos la variable que controla si se ha adivinado el n�mero
    adivinado = Falso
    
    // Repetimos el proceso hasta que el n�mero sea adivinado
    Mientras adivinado = Falso Hacer
        // Solicitamos al usuario que adivine el n�mero
        Escribir "Adivina un n�mero entre 1 y 10: "
        Leer intento
        
        // Verificamos si el intento es igual al n�mero secreto
        Si intento = numeroSecreto Entonces
            // Si es correcto, mostramos un mensaje y terminamos el bucle
            Escribir "�Felicidades! Adivinaste el n�mero."
            adivinado = Verdadero
        Sino
            // Si es incorrecto, mostramos un mensaje de error
            Escribir "Ese no es el n�mero correcto. Int�ntalo de nuevo."
        FinSi
    FinMientras
FinProceso


