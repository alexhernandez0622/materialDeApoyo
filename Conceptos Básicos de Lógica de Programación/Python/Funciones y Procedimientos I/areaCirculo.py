def area_circulo(radio):
    valordePi = 3.1416
    area = valordePi * (radio ** 2)
    return area

def ejercicio_funciones_2():
    radio = float(input("Escribe el radio: "))
    area = area_circulo(radio)
    print(area)

ejercicio_funciones_2()
