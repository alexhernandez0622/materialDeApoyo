// Revertir los elementos de un array/lista
Proceso RevertirArray
    Definir i Como Entero
    Definir numeros Como Entero[5]
    Definir numerosInvertidos Como Entero[5]
    
    // Llenar el array con 5 números
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir "Ingrese un número para la posición ", i, ": "
        Leer numeros[i]
    FinPara
    
    // Revertir los elementos del array
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        numerosInvertidos[i] <- numeros[6 - i]
    FinPara
    
    // Mostrar el array invertido
    Escribir "Array invertido: "
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir numerosInvertidos[i]
    FinPara
FinProceso
