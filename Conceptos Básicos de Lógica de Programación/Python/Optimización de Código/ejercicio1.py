# Dada una lista de elementos, optimiza la búsqueda de un elemento utilizando conjuntos (set).

# Lista original de elementos
lista = [5, 8, 12, 16, 23, 42, 8, 16]

# Convertir la lista a un conjunto para optimizar la búsqueda
elementos = set(lista)  # La conversión a set elimina duplicados y optimiza la búsqueda

# Definir el elemento a buscar
elemento_a_buscar = 23

# Verificar si el elemento está en el conjunto
encontrado = elemento_a_buscar in elementos  # La operación 'in' en sets es O(1) en promedio

# Imprimir el resultado de la búsqueda
print(encontrado)
