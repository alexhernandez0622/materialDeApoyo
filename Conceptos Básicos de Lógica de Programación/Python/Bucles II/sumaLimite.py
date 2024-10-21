# Programa que solicita al usuario ingresar números y los suma.
# El proceso continúa hasta que el usuario ingrese un número negativo.
suma = 0

# Leer el primer número
numero = float(input("Ingrese un número (negativo para terminar): "))

# Bucle while para leer números hasta que se ingrese un negativo
while numero >= 0:
    suma += numero
    numero = float(input("Ingrese otro número (negativo para terminar): "))

# Mostrar el resultado de la suma
print("La suma de los números ingresados es:", suma)
