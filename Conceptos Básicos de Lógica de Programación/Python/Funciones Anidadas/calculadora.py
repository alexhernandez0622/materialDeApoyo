def calculadora():
    """
    Realiza una operación matemática básica entre dos números ingresados por el usuario.
    
    Returns:
    float: El resultado de la operación.
    """
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (suma, resta, multiplicacion, division): ").lower()

    def suma():
        return a + b
    
    def resta():
        return a - b
    
    def multiplicacion():
        return a * b
    
    def division():
        return a / b if b != 0 else 'Error: División por cero'
    
    operaciones = {
        'suma': suma,
        'resta': resta,
        'multiplicacion': multiplicacion,
        'division': division
    }
    
    return operaciones.get(operacion, lambda: 'Operación inválida')()

# Ejemplo de uso
print(f"El resultado de la operación es: {calculadora()}")
