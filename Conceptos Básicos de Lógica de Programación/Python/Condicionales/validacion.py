# Ejercicio 7: Validar si la contraseña ingresada es correcta.

# Definir la contraseña correcta.
contraseña_correcta = "python123"

# Solicitar al usuario que ingrese la contraseña.
contraseña_ingresada = input("Ingresa la contraseña: ")

# Verificar si la contraseña ingresada es igual a la correcta.
if contraseña_ingresada == contraseña_correcta:
    print("Contraseña correcta, acceso concedido.")
else:
    print("Contraseña incorrecta, acceso denegado.")
