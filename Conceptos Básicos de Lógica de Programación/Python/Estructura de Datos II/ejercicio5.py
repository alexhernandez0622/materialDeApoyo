##  Dado un diccionario anidado, acceder y mostrar un valor específico.

# Diccionario anidado con información de una persona
persona = {
    'nombre': 'Juan',
    'edad': 30,
    'direccion': {
        'calle': 'Calle Falsa',
        'numero': 123,
        'ciudad': 'Springfield'
    }
}

# Acceder al valor específico del diccionario anidado (ciudad)
ciudad = persona['direccion']['ciudad']

# Imprimir el valor de la ciudad
print("La ciudad es:", ciudad)
