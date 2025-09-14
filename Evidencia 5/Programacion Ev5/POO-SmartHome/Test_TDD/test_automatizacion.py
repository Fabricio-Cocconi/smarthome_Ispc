import unittest
from core.automatizacion import ReglaAutomatizacion

class TestReglaAutomatizacion(unittest.TestCase):
    def test_evaluar_condicion_true(self):
        self.ejecutado = False
        def condicion():
            return True
        def accion():
            self.ejecutado = True
        regla = ReglaAutomatizacion(condicion, accion, "Prueba True")
        resultado = regla.evaluar()
        self.assertTrue(self.ejecutado)
        self.assertTrue(resultado)

    def test_evaluar_condicion_false(self):
        self.ejecutado = False
        def condicion():
            return False
        def accion():
            self.ejecutado = True
        regla = ReglaAutomatizacion(condicion, accion, "Prueba False")
        resultado = regla.evaluar()
        self.assertFalse(self.ejecutado)
        self.assertFalse(resultado)

if __name__ == "__main__":
    unittest.main()