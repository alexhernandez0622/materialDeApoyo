def calcular_area():
    """
    Calcula el área de un círculo o un rectángulo según la opción seleccionada.
    """
    opcion = input("¿Qué figura deseas calcular? (círculo/rectángulo): ").lower()
    
    def area_circulo(radio):
        import math
        return math.pi * radio ** 2
    
    def area_rectangulo(base, altura):
        return base * altura
    
    if opcion == "círculo":
        radio = float(input("Ingresa el radio del círculo: "))
        print(f"El área del círculo es: {area_circulo(radio)}")
    elif opcion == "rectángulo":
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")
    else:
        print("Opción inválida")

# Ejemplo de uso
calcular_area()
