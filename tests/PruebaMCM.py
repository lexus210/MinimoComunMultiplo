import unittest
from src.logica.OperacionesMCM import OperacionesEnteros
from src.logica.FaltanParametros import FaltanParametros

class PruebaOperacionesEnteros(unittest.TestCase):
    def test_MCM_dos_numeros(self):
        operacion = OperacionesEnteros([4, 6])
        self.assertEqual(operacion.calcularMCM(), 12)

    def test_MCM_tres_numeros(self):
        operacion = OperacionesEnteros([4, 6, 8])
        self.assertEqual(operacion.calcularMCM(), 24)

    def test_MCM_cuatro_numeros(self):
        operacion = OperacionesEnteros([4, 6, 8, 12])
        self.assertEqual(operacion.calcularMCM(), 24)

if __name__ == '__main__':
    unittest.main()
