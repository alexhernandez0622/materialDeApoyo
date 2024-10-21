# Dada una lista de cadenas, optimiza la concatenación de todas ellas en una sola cadena.

# Lista de cadenas a concatenar
cadenas = ["Hola", "mundo", "esto", "es", "Python"]

# Utilizar el método join en lugar de concatenación manual
resultado = " ".join(cadenas)  # join es más eficiente que usar operadores + repetidamente

# Imprimir la cadena concatenada
print(resultado)
