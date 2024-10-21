# Se espera eliminar las claves con valores negativos de un diccionario
valores = {'a': 5, 'b': -3, 'c': 10, 'd': -7}

for clave in valores:  # Error: no se puede eliminar directamente durante la iteración
    if valores[clave] < 0:
        del valores[clave]  # Error: RuntimeError al modificar el diccionario durante la iteración

print(valores)
