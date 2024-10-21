# Contar las cvocales

# # Definir una cadena
cadena = "programacion"  # Cadena de ejemplo

# Inicializar el contador de vocales
contador_vocales = 0  # Contador de vocales inicializado a 0

# Definir las vocales
vocales = "aeiou"  # Cadena con todas las vocales minúsculas

# Contar las vocales
for letra in cadena:  # Iterar sobre cada letra de la cadena
    if letra in vocales:  # Si la letra es una vocal
        contador_vocales += 1  # Incrementar el contador de vocales

# Imprimir el resultado
print("El número de vocales es:", contador_vocales)  # Muestra el número de vocales
