def calcular_area(base, altura):
    return base * altura / 2

def area_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    
    area = calcular_area(base, altura)
    print("El área del triángulo es:", area)

# Llamar a la función principal
area_triangulo()
