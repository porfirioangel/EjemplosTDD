# coding=utf-8

import unittest
from promedios import Promedios

class PromediosTest(unittest.TestCase):
    # Test fixtures
    def setUp(self):
        self.promedios = Promedios()

    def tearDown(self):
        pass

    def test_aprobado(self):
        res = self.promedios.get_status(6, 7, 8)
        self.assertEqual(res, "Aprobado")

    def test_reprobado(self):
        res = self.promedios.get_status(4, 5, 5)
        self.assertEqual(res, "Reprobado")

# Ejecuta las pruebas implementadas
if __name__ == '__main__': # pragma: no cover
    unittest.main()