# Dado un diccionario, optimiza la eliminación de claves con valores específicos.

# Diccionario original con claves y valores
datos = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Definir el valor a eliminar
valor_a_eliminar = 3

# Utilizar un diccionario por comprensión para filtrar las claves
datos_filtrados = {k: v for k, v in datos.items() if v != valor_a_eliminar}  # Se filtran las claves cuyos valores no son el valor_a_eliminar

# Imprimir el diccionario filtrado
print(datos_filtrados)

