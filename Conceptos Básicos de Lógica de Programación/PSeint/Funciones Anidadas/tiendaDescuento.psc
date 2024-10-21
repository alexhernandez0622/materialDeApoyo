Funcion descuento <- calcularDescuento(monto, categoria)
	Si categoria = "A" Entonces
		descuento <- monto * 0.1
	SiNo
		Si categoria = "B" Entonces
			descuento <- monto * 0.2
		SiNo
			descuento <- monto * 0.3
		Fin Si
	Fin Si
Fin Funcion
Algoritmo tiendaDescuento
	Definir monto, categoria Como Real
	Escribir "Ingrese el monto de la compra: "
	Leer monto
	Escribir "Ingrese la categoría del cliente (A, B o C): "
	Leer categoria
	
	Escribir "El descuento aplicado es: $", calcularDescuento(monto, categoria)
	Escribir "El monto a pagar es: $", monto - calcularDescuento(monto, categoria)
FinAlgoritmo
