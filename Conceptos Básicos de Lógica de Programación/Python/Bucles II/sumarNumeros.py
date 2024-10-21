# Ejercicio 2: Sumar números ingresados por el usuario hasta que ingrese un cero.

# Inicializar la variable suma.
suma = 0

# Utilizar un bucle while para pedir números hasta que se ingrese un cero.
while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break  # Salir del bucle si se ingresa un cero.
    suma += numero  # Sumar el número ingresado a la variable suma.

# Mostrar la suma total.
print(f"La suma total es: {suma}")
