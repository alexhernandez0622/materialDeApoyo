// funci�n en pseudoc�digo que devuelva el �rea de un c�rculo dado su radio. Recuerda que para calcular el area, la formula es ? * r2
Funcion area <- area_circulo ( radio )
	valordePi<-3.1416
	area<-valordePi*(radio^2)
FinFuncion
Algoritmo ejercicio_funciones_2
	Escribir "Escribe el radio"
	leer radio
	area<-area_circulo(radio)
	Escribir area
FinAlgoritmo
