# Ejercicio 6: Imprimir la tabla de multiplicar de un número ingresado por el usuario.

# Solicitar al usuario que ingrese un número.
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

# Utilizar un bucle for para generar la tabla de multiplicar.
for i in range(1, 11):
    resultado = numero * i  # Calcular el resultado de la multiplicación.
    print(f"{numero} x {i} = {resultado}")  # Mostrar el resultado en formato de tabla.
