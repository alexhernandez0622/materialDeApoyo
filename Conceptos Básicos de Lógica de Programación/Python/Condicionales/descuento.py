# Ejercicio 5: Calcular el descuento según el monto de una compra.

# Solicitar al usuario que ingrese el monto de la compra.
monto = float(input("Ingresa el monto de la compra: "))

# Aplicar un descuento basado en el monto ingresado.
if monto > 100:
    descuento = monto * 0.10  # 10% de descuento si el monto es mayor a 100
else:
    descuento = monto * 0.05  # 5% de descuento si el monto es 100 o menor

# Calcular y mostrar el monto final después del descuento.
monto_final = monto - descuento
print(f"El monto final después del descuento es: {monto_final}")
