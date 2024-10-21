def ordenar_lista():
    """
    Ordena una lista de números en orden ascendente o descendente según la opción seleccionada.
    """
    # Solicita al usuario que ingrese una lista de números separados por espacios y el .split nos ayuda a separar una cadena de texto en componentes individuales.
    numeros = list(map(int, input("Ingresa una lista de números separados por espacios: ").split()))
    
    # Solicita al usuario que indique si desea ordenar la lista en orden ascendente o descendente y convierte la entrada a minúsculas
    opcion = input("¿Ordenar en orden ascendente o descendente? (ascendente/descendente): ").lower()
    
    def ordenar_ascendente(lista):
        """
        Ordena una lista de números en orden ascendente.
        
        Args:
        lista (list): Lista de números a ordenar.
        
        Returns:
        list: Lista ordenada en orden ascendente.
        """
        # Usa la función sorted() para ordenar la lista en orden ascendente
        return sorted(lista)
    
    def ordenar_descendente(lista):
        """
        Ordena una lista de números en orden descendente.
        
        Args:
        lista (list): Lista de números a ordenar.
        
        Returns:
        list: Lista ordenada en orden descendente.
        """
        # Usa la función sorted() con el argumento reverse=True para ordenar la lista en orden descendente
        return sorted(lista, reverse=True)
    
    # Si la opción seleccionada es "ascendente", ordena la lista en orden ascendente y la imprime
    if opcion == "ascendente":
        print(f"La lista ordenada en orden ascendente es: {ordenar_ascendente(numeros)}")
    # Si la opción seleccionada es "descendente", ordena la lista en orden descendente y la imprime
    elif opcion == "descendente":
        print(f"La lista ordenada en orden descendente es: {ordenar_descendente(numeros)}")
    # Si la opción no es válida, imprime un mensaje de error
    else:
        print("Opción inválida")

# Ejemplo de uso de la función ordenar_lista
ordenar_lista()
