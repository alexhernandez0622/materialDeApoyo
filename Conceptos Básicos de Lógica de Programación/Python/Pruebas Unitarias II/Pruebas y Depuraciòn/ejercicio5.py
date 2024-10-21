# Se espera acceder a valores de un diccionario dado un conjunto de claves
persona = {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Madrid'}

for clave in ['nombre', 'edad', 'país']:  # Error: 'país' no está en el diccionario
    print(persona[clave])  # Error: KeyError si la clave no existe
