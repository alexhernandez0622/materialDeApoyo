# Ejercicio 3: Adivinar un número entre 1 y 10.
import random

# Generar un número secreto aleatorio entre 1 y 10.
numero_secreto = random.randint(1, 10)

# Inicializar la variable para el intento del usuario.
intento = None

# Utilizar un bucle while para seguir pidiendo números hasta que se adivine el correcto.
while intento != numero_secreto:
    intento = int(input("Adivina el número entre 1 y 10: "))
    if intento < numero_secreto:
        print("Demasiado bajo, intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto, intenta de nuevo.")

# Mensaje de éxito cuando se adivina el número.
print("¡Felicidades! Adivinaste el número.")
