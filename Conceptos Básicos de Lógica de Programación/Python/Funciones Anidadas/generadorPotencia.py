def generador_potencia(n):
    """
    Genera una función que eleva un número a la potencia n.
    
    Args:
    n (int): Potencia a la que se elevará el número.
    
    Returns:
    function: Función que eleva un número a la potencia n.
    """
    def potencia(x):
        """
        Eleva el número x a la potencia n.
        
        Args:
        x (int): Número a elevar.
        
        Returns:
        int: El resultado de x^n.
        """
        return x ** n
    
    return potencia

# Ejemplo de uso
elevar_al_cubo = generador_potencia(3)
print(elevar_al_cubo(4))  # Salida: 64
