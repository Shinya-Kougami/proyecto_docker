# test_calculadora.py
import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(calculadora.sumar(3, 2), 5)
        self.assertEqual(calculadora.sumar(-1, 1), 0)

    def test_restar(self):
        self.assertEqual(calculadora.restar(5, 2), 3)
        self.assertEqual(calculadora.restar(10, 10), 0)

    def test_multiplicar(self):
        self.assertEqual(calculadora.multiplicar(3, 3), 9)
        self.assertEqual(calculadora.multiplicar(-2, 4), -8)

    def test_dividir(self):
        self.assertEqual(calculadora.dividir(10, 2), 5)
        self.assertEqual(calculadora.dividir(9, 3), 3)
        with self.assertRaises(ValueError):
            calculadora.dividir(5, 0)

if __name__ == '__main__':
    unittest.main()