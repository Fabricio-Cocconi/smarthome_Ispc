import unittest
from core.dispositivo import Dispositivo

class TestDispositivo(unittest.TestCase):
    def test_estado_inicial(self):
        d = Dispositivo("Luz Sala", "luz")
        self.assertFalse(d.estado)

    def test_cambiar_estado(self):
        d = Dispositivo("Luz Sala", "luz")
        d.cambiar_estado(True)
        self.assertTrue(d.estado)
        d.cambiar_estado(False)
        self.assertFalse(d.estado)

    def test_toggle(self):
        d = Dispositivo("Luz Sala", "luz")
        d.toggle()
        self.assertTrue(d.estado)
        d.toggle()
        self.assertFalse(d.estado)

    def test_str(self):
        d = Dispositivo("Luz Sala", "luz")
        self.assertIn("Apagado", str(d))
        d.cambiar_estado(True)
        self.assertIn("Encendido", str(d))

if __name__ == "__main__":
    unittest.main()