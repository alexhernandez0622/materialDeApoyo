##  Calcula la suma de dos números.
def suma(a, b):
    def agregar():
        return a + b
    return agregar()

# Solicitar datos al usuario
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Mostrar el resultado
print("La suma es:", suma(a, b))
