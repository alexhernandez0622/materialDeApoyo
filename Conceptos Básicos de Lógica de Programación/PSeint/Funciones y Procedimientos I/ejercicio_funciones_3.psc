Funcion resultado = EsPar(n)
	Si n % 2 = 0 Entonces
		resultado = Verdadero
	Sino
		resultado = Falso
	FinSi
FinFuncion
Algoritmo ejercicio_funciones_3
    Definir n Como Entero
	
    Escribir "Ingresa un número: "
	Leer n
	
	Si EsPar(n) Entonces
		Escribir "Es par"
	Sino
		Escribir "Es impar"
	FinSi
FinAlgoritmo