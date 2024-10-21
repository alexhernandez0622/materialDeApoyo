def determinar_mayor(a, b, c):
    if a > b and a > c:
        mayor = a
    elif b > a and b > c:
        mayor = b
    else:
        mayor = c
    return mayor

def mayor_tres_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    mayor = determinar_mayor(num1, num2, num3)
    print("El mayor de los tres números es:", mayor)

# Llamar a la función principal
mayor_tres_numeros()
