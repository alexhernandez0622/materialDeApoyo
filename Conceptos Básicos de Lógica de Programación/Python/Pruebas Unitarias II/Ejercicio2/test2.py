import unittest

from ejercicio2 import es_par
class TestEsPar(unittest.TestCase):
    def test_numero_par(self):
        """
        Test para verificar que un número par sea identificado correctamente.
        """
        numero = 4  # Valor de entrada para el test.
        self.assertTrue(es_par(numero))  # Verifica que la función es_par devuelva True para un número par.

    def test_numero_impar(self):
        """
        Test para verificar que un número impar sea identificado correctamente.
        """
        numero = 5  # Valor de entrada para el test.
        self.assertFalse(es_par(numero))  # Verifica que la función es_par devuelva False para un número impar.

if __name__ == '__main__':
    unittest.main()  # Ejecuta los tests cuando se corre el script.