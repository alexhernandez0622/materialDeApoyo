# Imprimir una tabla de multiplicar

# Definir el número para la tabla de multiplicar
numero = 7  # Número del que se quiere la tabla de multiplicar

# Imprimir la tabla de multiplicar
print("Tabla de multiplicar del", numero)  # Encabezado de la tabla
for i in range(1, 11):  # Iterar del 1 al 10
    print(numero, "x", i, "=", numero * i)  # Mostrar la multiplicación y su resultado


