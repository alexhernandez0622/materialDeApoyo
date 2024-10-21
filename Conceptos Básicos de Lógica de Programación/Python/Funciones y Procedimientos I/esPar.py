def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def ejercicio_funciones_3():
    n = int(input("Ingresa un número: "))
    
    if es_par(n):
        print("Es par")
    else:
        print("Es impar")

ejercicio_funciones_3()
