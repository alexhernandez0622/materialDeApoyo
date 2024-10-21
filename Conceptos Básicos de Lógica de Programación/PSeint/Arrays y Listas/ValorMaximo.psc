// Encuentra el valor máximo en un array/lista
Proceso ValorMaximoArray
    Definir n, i, maximo Como Entero
    Definir numeros Como Entero[5]
    
    // Llenar el array con 5 números
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir "Ingrese un número para la posición ", i, ": "
        Leer numeros[i]
    FinPara
    
    // Inicializar el máximo con el primer elemento
    maximo <- numeros[1]
    
    // Encontrar el valor máximo en el array
    Para i <- 2 Hasta 5 Con Paso 1 Hacer
        Si numeros[i] > maximo Entonces
            maximo <- numeros[i]
        FinSi
    FinPara
    
    // Mostrar el valor máximo
    Escribir "El valor máximo es: ", maximo
FinProceso
