def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    pi = 3.14  # Valor aproximado de PI, podría ser más preciso usando math.pi
    area = pi * radio ^ 2  # Error: operador incorrecto para elevar al cuadrado
    return area

def main():
    # Error: falta de validación del tipo de entrada
    radio = input("Ingrese el radio del círculo: ")
    area = calcular_area_circulo(radio)  # Error: no se convierte a número
    print(f"El área del círculo es: {area}")

if __name__ == "__main__":
    main()  
