# Suma de los elementos de una lista

# Inicialización de la lista
numeros = []

# Llenar la lista con 5 números
for i in range(5):
    num = int(input(f"Ingrese un número para la posición {i+1}: "))
    numeros.append(num)

# Sumar todos los elementos de la lista
suma = sum(numeros)

# Mostrar la suma total
print("La suma de los elementos es:", suma)

# Encuentra el valor máximo en una lista

# Inicialización de la lista
numeros = []

# Llenar la lista con 5 números
for i in range(5):
    num = int(input(f"Ingrese un número para la posición {i+1}: "))
    numeros.append(num)

# Encontrar el valor máximo en la lista
maximo = max(numeros)

# Mostrar el valor máximo
print("El valor máximo es:", maximo)


# Promedio de los elementos de una lista

# Inicialización de la lista
numeros = []

# Llenar la lista con 5 números
for i in range(5):
    num = int(input(f"Ingrese un número para la posición {i+1}: "))
    numeros.append(num)

# Sumar todos los elementos de la lista
suma = sum(numeros)

# Calcular el promedio
promedio = suma / len(numeros)

# Mostrar el promedio
print("El promedio de los elementos es:", promedio)


# Revertir los elementos de una lista

# Inicialización de la lista
numeros = []

# Llenar la lista con 5 números
for i in range(5):
    num = int(input(f"Ingrese un número para la posición {i+1}: "))
    numeros.append(num)

# Revertir los elementos de la lista
numeros_invertidos = numeros[::-1]

# Mostrar la lista invertida
print("Lista invertida:", numeros_invertidos)

