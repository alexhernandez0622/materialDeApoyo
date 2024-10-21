# Ejercicio 5: Crear una función que invierta una cadena de texto.

def invertir_cadena(cadena):
    """
    Esta función invierte una cadena de texto.
    
    Parámetros:
    cadena (str): La cadena de texto que se desea invertir.
    
    Retorna:
    str: La cadena invertida.
    """
    return cadena[::-1]

# Probar la función con una cadena de texto.
cadena_invertida = invertir_cadena("Python")
print(f"La cadena invertida de 'Python' es: {cadena_invertida}")
