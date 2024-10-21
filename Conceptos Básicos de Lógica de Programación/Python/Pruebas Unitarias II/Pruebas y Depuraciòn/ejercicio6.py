# Se espera agregar elementos a un diccionario desde una lista de claves
claves = ['x', 'y', 'z']
valores = (10, 20, 30)  # Error: los valores están en una tupla

diccionario = {}

for i in range(len(claves)):
    diccionario[claves[i]] = valores[i]  # Error: `valores` es un objeto iterable, pero podría causar problemas si son de diferente longitud

print(diccionario)
