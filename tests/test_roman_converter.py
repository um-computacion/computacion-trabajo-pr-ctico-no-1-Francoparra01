# Importamos la biblioteca de testing estándar de Python
import unittest

# Importamos la función que vamos a testear
# Por ahora todavía no está implementada
from src.roman_converter import decimal_to_roman

# Creamos una clase para agrupar nuestras pruebas
class TestRomanConverter(unittest.TestCase):

    # Test de números romanos básicos
    def test_basic_numbers(self):
        self.assertEqual(decimal_to_roman(1), "I")  # 1 => I
        self.assertEqual(decimal_to_roman(5), "V")  # 5 => V
        self.assertEqual(decimal_to_roman(10), "X")  # 10 => X

    # Test de reglas de sustracción
    def test_subtraction_rules(self):
        self.assertEqual(decimal_to_roman(4), "IV")   # 4 => IV
        self.assertEqual(decimal_to_roman(9), "IX")   # 9 => IX
        self.assertEqual(decimal_to_roman(40), "XL")  # 40 => XL
        self.assertEqual(decimal_to_roman(90), "XC")  # 90 => XC

    # Test de números complejos
    def test_complex_numbers(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")      # 40 + 9
        self.assertEqual(decimal_to_roman(99), "XCIX")      # 90 + 9
        self.assertEqual(decimal_to_roman(499), "CDXCIX")   # 400 + 90 + 9
        self.assertEqual(decimal_to_roman(999), "CMXCIX")   # 900 + 90 + 9
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")  # Máximo permitido

# Este bloque hace que las pruebas se ejecuten si corrés el archivo directamente
if __name__ == '__main__':
    unittest.main()
