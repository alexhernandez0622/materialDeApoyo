## Dada una lista con elementos duplicados, eliminar los duplicados y mostrar la lista sin duplicados.

# Lista con elementos duplicados
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# Convertir la lista a un conjunto para eliminar duplicados y luego volver a lista
lista_sin_duplicados = list(set(lista_con_duplicados))

# Imprimir la lista sin duplicados
print("Lista sin elementos duplicados:", lista_sin_duplicados)
