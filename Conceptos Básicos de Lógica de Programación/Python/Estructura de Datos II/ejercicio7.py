Diccionario = {
    "venezuela": "venezolano",
    "colombia": "colombiano",
    "ecuador": "ecuatoriano",
    "panama": "panameño"
}

print("Seleccione una opción para saber su pronombre:")
print("1. venezuela")
print("2. colombia")
print("3. ecuador")
print("4. panama")
print("5. mostrar todos los países")

pais = input("")

# Mostrar todos los países
if pais == "5":
    for i, (clave, valor) in enumerate(Diccionario.items(), start=1):
        print(f"Número: {i}, País: {clave}, Pronombre: {valor}")
else:
    # Encontrar el índice correspondiente al país seleccionado
    for i, (clave, valor) in enumerate(Diccionario.items(), start=1):
        if (pais == "1" and clave == "venezuela") or \
           (pais == "2" and clave == "colombia") or \
           (pais == "3" and clave == "ecuador") or \
           (pais == "4" and clave == "panama"):
            print(f"Número: {i}, Pronombre para {clave.capitalize()}: {valor}")
            break
    else:
        print("Opción no válida")
