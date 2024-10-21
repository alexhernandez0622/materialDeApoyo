Funcion mayor <- determinarMayor(a, b, c)
	Si a > b Y a > c Entonces
		mayor <- a
	SiNo
		Si b > a Y b > c Entonces
			mayor <- b
		SiNo
			mayor <- c
		Fin Si
	Fin Si
Fin Funcion

Algoritmo mayorTresNumeros
	Definir num1, num2, num3 Como Real
	Escribir "Ingrese el primer número: "
	Leer num1
	Escribir "Ingrese el segundo número: "
	Leer num2
	Escribir "Ingrese el tercer número: "
	Leer num3
	
	Escribir "El mayor de los tres números es: ", determinarMayor(num1, num2, num3)
FinAlgoritmo
