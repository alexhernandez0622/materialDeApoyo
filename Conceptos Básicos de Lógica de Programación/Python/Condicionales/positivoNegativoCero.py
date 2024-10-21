# Ejercicio 1: Verificar si un número es positivo, negativo o cero.

# Solicitar al usuario que ingrese un número.
numero = int(input("Ingresa un número: "))

# Evaluar si el número es positivo, negativo o cero.
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
