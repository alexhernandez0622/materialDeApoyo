# Ejercicio 1: Crear una función que reciba un número y devuelva su cuadrado.

def calcular_cuadrado(numero):
    """
    Esta función recibe un número y devuelve su cuadrado.
    
    Parámetros:
    numero (int, float): El número del que se quiere calcular el cuadrado.
    
    Retorna:
    int, float: El cuadrado del número dado.
    """
    return numero ** 2

# Probar la función con un número.
resultado = calcular_cuadrado(5)
print(f"El cuadrado de 5 es: {resultado}")
