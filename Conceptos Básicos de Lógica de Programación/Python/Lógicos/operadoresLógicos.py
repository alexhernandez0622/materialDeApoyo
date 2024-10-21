# Ejercicio 1: Verificación de igualdad
# Este ejercicio verifica si dos números son iguales

# Solicitamos los dos números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Comparamos si num1 es igual a num2
son_iguales = num1 == num2

# Imprimimos el resultado
print(f"¿Los números son iguales? {son_iguales}")

# Ejercicio 2: Verificación de desigualdad
# Este ejercicio verifica si dos cadenas de texto son diferentes

# Solicitamos las dos cadenas de texto al usuario
cadena1 = input("Ingrese la primera cadena de texto: ")
cadena2 = input("Ingrese la segunda cadena de texto: ")

# Comparamos si cadena1 es diferente a cadena2
son_diferentes = cadena1 != cadena2

# Imprimimos el resultado
print(f"¿Las cadenas son diferentes? {son_diferentes}")

# Ejercicio 3: Uso del operador "and"
# Este ejercicio verifica si un número está en un rango específico

# Solicitamos el número al usuario
numero = int(input("Ingrese un número: "))

# Verificamos si el número está entre 10 y 20
esta_en_rango = numero >= 10 and numero <= 20

# Imprimimos el resultado
print(f"¿El número está entre 10 y 20? {esta_en_rango}")

# Ejercicio 4: Uso del operador "or"
# Este ejercicio verifica si una persona es mayor de edad o si tiene un permiso especial

# Solicitamos la edad de la persona al usuario
edad = int(input("Ingrese la edad: "))

# Solicitamos si tiene un permiso especial
permiso_especial = input("¿Tiene un permiso especial? (s/n): ").lower() == 's'

# Verificamos si la persona es mayor de edad o si tiene un permiso especial
puede_entrar = edad >= 18 or permiso_especial

# Imprimimos el resultado
print(f"¿La persona puede entrar? {puede_entrar}")

# Ejercicio 5: Uso de la negación "not"
# Este ejercicio verifica si un usuario no tiene acceso a una zona restringida

# Solicitamos si el usuario tiene acceso
tiene_acceso = input("¿El usuario tiene acceso? (s/n): ").lower() == 's'

# Usamos la negación para verificar si no tiene acceso
no_tiene_acceso = not tiene_acceso

# Imprimimos el resultado
print(f"¿El usuario no tiene acceso? {no_tiene_acceso}")

# Ejercicio 6: Combinación de operadores lógicos y relacionales
# Este ejercicio verifica si un número es positivo, par y menor que 50

# Solicitamos un número al usuario
numero = int(input("Ingrese un número: "))

# Verificamos si el número cumple las tres condiciones
cumple_condiciones = numero > 0 and numero % 2 == 0 and numero < 50

# Imprimimos el resultado
print(f"¿El número es positivo, par y menor que 50? {cumple_condiciones}")

