# Ejercicio 6: Pedir al usuario que ingrese una contraseña hasta que sea correcta.

# Definir la contraseña correcta.
contraseña_correcta = "python123"

# Inicializar la variable para la contraseña ingresada.
contraseña_ingresada = ""

# Utilizar un bucle while para seguir pidiendo la contraseña hasta que sea correcta.
while contraseña_ingresada != contraseña_correcta:
    contraseña_ingresada = input("Ingresa la contraseña: ")
    if contraseña_ingresada != contraseña_correcta:
        print("Contraseña incorrecta, intenta de nuevo.")

# Mensaje de éxito cuando se ingresa la contraseña correcta.
print("Contraseña correcta, acceso concedido.")