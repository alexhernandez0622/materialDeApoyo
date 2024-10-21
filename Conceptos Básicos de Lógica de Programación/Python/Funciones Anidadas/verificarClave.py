## Verifica si una contraseña cumple con los requisitos mínimos.
def verificar_contrasena():
    contrasena = input("Ingresa la contraseña: ")
    def longitud_valida():
        return len(contrasena) >= 8
    def contiene_numero():
        return any(char.isdigit() for char in contrasena)
    return longitud_valida() and contiene_numero()

# Ejemplo de uso
if verificar_contrasena():
    print("La contraseña es segura.")
else:
    print("La contraseña no cumple con los requisitos de seguridad.")
