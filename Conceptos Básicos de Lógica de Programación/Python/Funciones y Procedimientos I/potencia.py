def potencia(base, exponente):
    resultado = base ** exponente
    return resultado

def ejercicio_funciones_1():
    base = float(input("Introduce la base: "))
    exponente = float(input("Introduce el exponente: "))
    resultado = potencia(base, exponente)
    print(resultado)

ejercicio_funciones_1()
