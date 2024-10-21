# Se espera crear una lista con las sumas de pares de tuplas
tuplas = [(1, 2), (3, 4), (5, 6)]
suma_tuplas = []

for a, b, c in tuplas:  # Error: se están desempaquetando 3 valores en lugar de 2
    suma_tuplas.append(a + b)

print(suma_tuplas)
