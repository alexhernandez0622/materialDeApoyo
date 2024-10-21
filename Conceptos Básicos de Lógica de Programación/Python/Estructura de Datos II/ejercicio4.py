# Ejercicio 4: Iterar sobre las claves y valores de un diccionario

# Creación de un diccionario
inventario = {
    "manzanas": 10,
    "naranjas": 8,
    "bananas": 5
}

# Iterar sobre el diccionario para imprimir cada clave y su valor asociado
for fruta, cantidad in inventario.items():
    print(f"Tenemos {cantidad} {fruta}")
