# Dado un diccionario, optimiza el código para encontrar la clave con el valor mínimo.

# Definir el diccionario con claves y valores
puntuaciones = {'Juan': 82, 'Ana': 91, 'Luis': 77, 'Maria': 89}

# Utilizar la función min con un criterio (key) para encontrar la clave con el valor mínimo
clave_minima = min(puntuaciones, key=puntuaciones.get)  # key=puntuaciones.get utiliza los valores como criterio de comparación

# Imprimir la clave con el valor mínimo
print(clave_minima)
