import unittest

from ejercicio3 import calcular_cuadrado
class TestCalcularCuadrado(unittest.TestCase):
    def test_cuadrado_positivo(self):
        """
        Test para verificar que el cuadrado de un número positivo se calcula correctamente.
        """
        numero = 3  # Valor de entrada para el test.
        self.assertEqual(calcular_cuadrado(numero), 9)  # Verifica que el resultado del cálculo sea igual a 9 (3 * 3).

    def test_cuadrado_negativo(self):
        """
        Test para verificar que el cuadrado de un número negativo se calcula correctamente.
        """
        numero = -3  # Valor de entrada para el test.
        self.assertEqual(calcular_cuadrado(numero), 9)  # Verifica que el resultado del cálculo sea igual a 9 (-3 * -3).

if __name__ == '__main__':
    unittest.main()  # Ejecuta los tests cuando se corre el script.