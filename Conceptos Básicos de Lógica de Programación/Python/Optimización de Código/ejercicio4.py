# Dados dos listas, optimiza el código para encontrar la intersección de elementos.

# Definir las dos listas
lista1 = [1, 3, 5, 7, 9]
lista2 = [3, 4, 5, 6, 7]

# Convertir las listas a conjuntos para aprovechar la eficiencia de las operaciones de conjuntos
interseccion = list(set(lista1) & set(lista2))  # & realiza la intersección entre los dos conjuntos

# Imprimir la lista de elementos comunes
print(interseccion)
