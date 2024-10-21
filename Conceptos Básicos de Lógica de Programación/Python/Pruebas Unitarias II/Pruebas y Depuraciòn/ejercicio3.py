# Se espera sumar todos los números de una lista
numeros = [1, 2, '3', 4, 5]  # Error: '3' es un string, no un entero
suma_total = 0

for n in numeros:
    suma_total += n  # Error: TypeError cuando se intenta sumar entero con string

print("La suma total es", suma_total)
