# coding=utf-8

import unittest
from descuentos import Descuentos


class DescuentosTest(unittest.TestCase):
    
    # Test fixtures
    def setUp(self):
        self.descuentos = Descuentos()

    def tearDown(self):
        pass

    def test_compra_mayor_5000(self):
        res = self.descuentos.get_descuento(6500)
        self.assertEqual(res, 1950)

    def test_compra_mayor_3000(self):
        res = self.descuentos.get_descuento(3500)
        self.assertEqual(res, 700)

    def test_compra_mayor_1000(self):
        res = self.descuentos.get_descuento(1500)
        self.assertEqual(res, 150)

    def test_compra_menor_100(self):
        res = self.descuentos.get_descuento(900)
        self.assertEqual(res, 0)

# Ejecuta las pruebas implementadas
if __name__ == '__main__': # pragma: no cover
    unittest.main()