# Ejercicio 2: Crear una función que determine si un número es par.

def es_par(numero):
    """
    Esta función verifica si un número es par.
    
    Parámetros:
    numero (int): El número que se quiere verificar.
    
    Retorna:
    bool: True si el número es par, False si es impar.
    """
    return numero % 2 == 0

# Probar la función con un número.
resultado = es_par(8)
print(f"¿El número 8 es par? {resultado}")
