# Ejercicio 1: Verificar si un número es positivo, negativo o cero

# Entrada: Un número entero
numero = int(input("Ingresa un número: "))

# Condición anidada para verificar si el número es positivo, negativo o cero
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
    
    # Ejercicio 2: Determinar si un número es par o impar y si es mayor que 10

# Entrada: Un número entero
numero = int(input("Ingresa un número: "))

# Condición múltiple para verificar si el número es par o impar
if numero % 2 == 0:
    if numero > 10:
        print("El número es par y mayor que 10.")
    else:
        print("El número es par y menor o igual que 10.")
else:
    if numero > 10:
        print("El número es impar y mayor que 10.")
    else:
        print("El número es impar y menor o igual que 10.")

# Ejercicio 3: Clasificación de edad

# Entrada: La edad de una persona
edad = int(input("Ingresa tu edad: "))

# Condición anidada para clasificar la edad
if edad < 13:
    print("Eres un niño.")
elif 13 <= edad < 18:
    print("Eres un adolescente.")
elif 18 <= edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")

# Ejercicio 4: Calificación de un examen

# Entrada: La calificación de un examen (0 a 100)
calificacion = int(input("Ingresa tu calificación: "))

# Condición anidada para determinar la nota según la calificación
if calificacion >= 90:
    print("Obtuviste una de Excelente")
elif calificacion >= 80:
    print("Obtuviste una de Sobresaliente")
elif calificacion >= 70:
    print("Obtuviste una de Aceptable ")
elif calificacion >= 60:
    print("Obtuviste una de Pasable")
else:
    print("Obtuviste un de Insuficiente")
