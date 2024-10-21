import unittest
from ejercicio1 import suma

## self es una parte fundamental de la estructura de las pruebas unitarias en Python, proporcionando un medio para gestionar el estado y las funciones dentro de las pruebas.
import unittest
from ejercicio1 import suma
## TestCase  es una clase de la biblioteca unittest de Python que facilita la escritura y ejecución de pruebas unitarias. Nos ayuda a crear casos para probar si funcionan o no funcionan
class TestSuma(unittest.TestCase):
    def setUp(self):
        # Solicitar datos por consola antes de cada prueba
        self.a = int(input("Ingrese el primer número: "))
        self.b = int(input("Ingrese el segundo número: "))

    def test_suma_positivos(self):
        """Prueba con dos números positivos."""
        resultado_esperado = self.a + self.b
        self.assertEqual(suma(self.a, self.b), resultado_esperado)

    def test_suma_negativos(self):
        """Prueba con dos números negativos."""
        resultado_esperado = self.a + self.b
        self.assertEqual(suma(self.a, self.b), resultado_esperado)

    def test_suma_cero(self):
        """Prueba con un cero y un número positivo o negativo."""
        resultado_esperado = self.a + self.b
        self.assertEqual(suma(self.a, self.b), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
