// Suma de los elementos de un array/lista
Proceso SumarElementosArray
    Definir n, i, suma Como Entero
    Definir numeros Como Entero[5]
    
    suma <- 0
    
    // Llenar el array con 5 números
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir "Ingrese un número para la posición ", i, ": "
        Leer numeros[i]
    FinPara
    
    // Sumar todos los elementos del array
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        suma <- suma + numeros[i]
    FinPara
    
    // Mostrar la suma total
    Escribir "La suma de los elementos es: ", suma
FinProceso

