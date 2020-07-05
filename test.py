import unittest
import logging

from silabeador.silabeador import separar_silabas

def setUpModule():
    logging.basicConfig(level=logging.DEBUG)

class TestSilabeador(unittest.TestCase):
    def test_2(self): # Las consonantes solas no forman sílabas
        r1 = separar_silabas("mano")
        r2 = separar_silabas("pena")
        self.assertEqual(len(r1), 2)
        self.assertEqual(len(r2), 2)

    def test_3(self): # Una consonante entre dos vocales forma la sílaba con la vocal que le sigue, es decir con la segunda sílaba.
        r1 = separar_silabas("seca")
        r2 = separar_silabas("salón")
        self.assertEqual(len(r1), 2)
        self.assertEqual(len(r2), 2)

    def test_4(self): # Cuando se tiene dos consonantes entre vocales, la primera va con la sílaba anterior y la segunda con la sílaba siguiente, con excepción de los grupos bl, br, dr, cr, cl, fr, fl, gr, gl, pl, pr, tr y dr.
        r1 = separar_silabas("gimnasio")
        r2 = separar_silabas("acróstico")
        r3 = separar_silabas("calcificación")
        r4 = separar_silabas("atrae")
        self.assertEqual(len(r1), 3)
        self.assertEqual(len(r2), 4)
        self.assertEqual(len(r3), 5)
        self.assertEqual(len(r4), 23)
