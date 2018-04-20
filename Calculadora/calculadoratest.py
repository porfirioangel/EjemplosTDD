# coding=utf-8

import unittest
from calculadora import Calculadora

class CaculadoraTest(unittest.TestCase):
    # Test fixtures
    def setUp(self):
        self.calc = Calculadora()

    def tearDown(self):
        pass

    def test_suma_positivos_1(self):
        res = self.calc.sumar(2, 2)
        self.assertEqual(res, 4)

    def test_resta_positivo_negativo(self):
        res = self.calc.restar(2, -5)
        self.assertEqual(res, 7)

# Ejecuta las pruebas implementadas
if __name__ == '__main__':
    unittest.main()