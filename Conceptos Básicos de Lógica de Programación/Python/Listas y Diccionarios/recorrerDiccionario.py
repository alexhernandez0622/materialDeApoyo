# Ejercicio 7: Recorrer un diccionario e imprimir sus claves y valores.

# Crear un diccionario con información de varios productos.
productos = {
    "manzana": 1.20,
    "banana": 0.50,
    "cereza": 2.00
}

# Recorrer el diccionario e imprimir cada clave y su valor.
for producto, precio in productos.items():
    print(f"Producto: {producto}, Precio: {precio}")
