# Crear un diccionario con información de personas
personas = {
    "Juan": {"edad": 25, "ciudad": "Madrid"},
    "Ana": {"edad": 22, "ciudad": "Barcelona"},
    "Luis": {"edad": 30, "ciudad": "Valencia"}
}

# Agregar una nueva persona al diccionario
personas["Carlos"] = {"edad": 28, "ciudad": "Sevilla"}

# Imprimir la información de todas las personas
for nombre, info in personas.items():
    print(f"Nombre: {nombre}, Edad: {info['edad']}, Ciudad: {info['ciudad']}")


# Crear un diccionario donde los valores son tuplas
ventas = {
    "ProductoA": (10, 150),  # (cantidad, precio_unitario)
    "ProductoB": (5, 300),
    "ProductoC": (12, 50)
}

# Calcular y mostrar el total de ventas por producto
for producto, (cantidad, precio_unitario) in ventas.items():
    total = cantidad * precio_unitario
    print(f"Total ventas para {producto}: {total}")

# Crear una lista de tuplas
estudiantes = [("Ana", 8.5), ("Luis", 9.0), ("Carlos", 7.8)]

# Imprimir la lista de estudiantes y sus notas
for nombre, nota in estudiantes:
    print(f"Nombre: {nombre}, Nota: {nota}")
