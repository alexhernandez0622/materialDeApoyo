Algoritmo CalificacionFinal
	Definir examen1, examen2, examen3, promedio Como Real
	
    // Solicitar las calificaciones de los tres ex�menes
    Escribir "Ingrese la calificaci�n del examen 1: "
    Leer examen1
    Escribir "Ingrese la calificaci�n del examen 2: "
    Leer examen2
    Escribir "Ingrese la calificaci�n del examen 3: "
    Leer examen3
	
    // Calcular el promedio
    promedio = (examen1 + examen2 + examen3) / 3
	
    // Determinar si el estudiante aprob� o reprob�
    Si promedio >= 10 Entonces
        Escribir "El estudiante aprob� con un promedio de: ", promedio
    Sino
        Escribir "El estudiante reprob� con un promedio de: ", promedio
    FinSi
FinAlgoritmo
