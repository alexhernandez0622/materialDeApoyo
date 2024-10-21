
# Encontrar el mayor de tres números

# Solicitar los tres números al usuario
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

# Encontrar el mayor número
mayor = a  # Suponer que el mayor es el primer número
if b > mayor:  # Si el segundo número es mayor que el actual mayor
    mayor = b  # Actualizar el mayor
if c > mayor:  # Si el tercer número es mayor que el actual mayor
    mayor = c  # Actualizar el mayor

# Imprimir el resultado
print("El mayor número es:", mayor)  # Muestra el mayor número
