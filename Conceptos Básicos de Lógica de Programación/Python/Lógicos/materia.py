# Solicitar la primera nota al usuario
nota1 = float(input("Ingresa la primera nota: "))

# Solicitar la segunda nota al usuario
nota2 = float(input("Ingresa la segunda nota: "))

# Solicitar la tercera nota al usuario
nota3 = float(input("Ingresa la tercera nota: "))

# Calcular el promedio de las tres notas
promedio = (nota1 + nota2 + nota3) / 3

# Imprimir el promedio calculado
print(f"El promedio de las tres notas es: {promedio:.2f}")

# Verificar si el promedio es mayor o igual a 3.0
if promedio >= 3.0:
    print("Aprobaste")
else:
    print("No aprobaste")
