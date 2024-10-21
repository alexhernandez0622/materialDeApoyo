// Encuentra el valor m�ximo en un array/lista
Proceso ValorMaximoArray
    Definir n, i, maximo Como Entero
    Definir numeros Como Entero[5]
    
    // Llenar el array con 5 n�meros
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir "Ingrese un n�mero para la posici�n ", i, ": "
        Leer numeros[i]
    FinPara
    
    // Inicializar el m�ximo con el primer elemento
    maximo <- numeros[1]
    
    // Encontrar el valor m�ximo en el array
    Para i <- 2 Hasta 5 Con Paso 1 Hacer
        Si numeros[i] > maximo Entonces
            maximo <- numeros[i]
        FinSi
    FinPara
    
    // Mostrar el valor m�ximo
    Escribir "El valor m�ximo es: ", maximo
FinProceso
