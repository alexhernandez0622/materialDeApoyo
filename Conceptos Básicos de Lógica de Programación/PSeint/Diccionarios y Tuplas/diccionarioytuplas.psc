Algoritmo diccionario_y_tuplas
    Definir personas Como Caracter
    Definir info Como Caracter
	
    // Crear un diccionario (en PSeInt se simula con una lista de registros)
    Definir personas Como Registro
	nombre Como Caracter
	edad Como Entero
	ciudad Como Caracter
Fin Registro

// Agregar datos al diccionario
personas["Juan"] <- Registro("Juan", 25, "Madrid")
personas["Ana"] <- Registro("Ana", 22, "Barcelona")
personas["Luis"] <- Registro("Luis", 30, "Valencia")

// Agregar una nueva persona
personas["Carlos"] <- Registro("Carlos", 28, "Sevilla")

// Imprimir la información de todas las personas
Para Cada persona En personas Hacer
	Escribir "Nombre: ", persona.nombre, ", Edad: ", persona.edad, ", Ciudad: ", persona.ciudad
FinPara
FinAlgoritmo
