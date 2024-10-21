# Ejercicio 3: Crear un procedimiento que reciba una lista de nombres y los imprima.

def imprimir_nombres(nombres):
    """
    Este procedimiento imprime cada nombre en una lista de nombres.
    
    Parámetros:
    nombres (list): Lista de nombres (str) que se desean imprimir.
    """
    for nombre in nombres:
        print(nombre)

# Probar el procedimiento con una lista de nombres.
lista_nombres = ["Ana", "Luis", "Carlos", "María"]
imprimir_nombres(lista_nombres)
