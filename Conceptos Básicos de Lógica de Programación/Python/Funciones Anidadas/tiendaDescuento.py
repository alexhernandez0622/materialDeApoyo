##  Aplica un descuento a un precio y calcula el precio final.
def aplicar_descuento():
    """
    Aplica un descuento a un precio ingresado por el usuario y calcula el precio final.
    """
    precio = float(input("Ingresa el precio original del producto: "))
    descuento = float(input("Ingresa el porcentaje de descuento: "))

    def calcular_precio_final():
        return precio - (precio * (descuento / 100))
    return calcular_precio_final()

# Ejemplo de uso
print(f"El precio final después del descuento es: {aplicar_descuento()}")

