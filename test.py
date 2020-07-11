import unittest
import logging

from repentista.silabeador import separar_silabas
from repentista.versometro import medir_verso

def setUpModule():
    logging.basicConfig(level=logging.DEBUG)


class TestRepentista(unittest.TestCase):
    
    # c + v : 
    # Las consonantes solas no forman sílabas
    def test_2(self): 
        r1 = separar_silabas("mano")
        r2 = separar_silabas("pena")
        self.assertEqual(len(r1), 2)
        self.assertEqual(len(r2), 2)

    # c + v + c : 
    # Una consonante entre dos vocales forma la sílaba con la vocal que le sigue, 
    # es decir con la segunda sílaba.
    def test_3(self): 
        r1 = separar_silabas("seca")
        r2 = separar_silabas("salón")
        self.assertEqual(len(r1), 2)
        self.assertEqual(len(r2), 2)

    # v + c + c + v
    # Cuando se tiene dos consonantes entre vocales, la primera va con la sílaba anterior y la segunda con la sílaba siguiente, 
    # con excepción de los grupos bl, br, dr, cr, cl, fr, fl, gr, gl, pl, pr, tr y dr.
    def test_4(self): 
        r1 = separar_silabas("gimnasio")
        r2 = separar_silabas("acróstico")
        r3 = separar_silabas("calcificación")
        r4 = separar_silabas("atrae")
        self.assertEqual(len(r1), 3)
        self.assertEqual(len(r2), 4)
        self.assertEqual(len(r3), 5)
        self.assertEqual(len(r4), 3)

    # grupos consonanticos:
    # Las combinaciones de consonantes bl, br, dr, cr, cl, fl, fr, gl, gr, tr, pl y pr no se separan de la vocal que les sigue. Observa con mucho cuidado los siguientes ejemplos y asegúrate que los entiendes.
    def test_5(self):
        r1 = separar_silabas("playa")
        r2 = separar_silabas("premiación")
        r3 = separar_silabas("padres")
        r4 = separar_silabas("transgresión")
        self.assertEqual(len(r1), 2)
        self.assertEqual(len(r2), 3)
        self.assertEqual(len(r3), 2)
        self.assertEqual(len(r4), 3)
    
    # v + c + c + c + v
    # Cuando tienes tres consonantes juntas, las dos primeras van con la vocal anterior y la tercera con la siguiente vocal.
    def test_6(self):
        r1 = separar_silabas("institución")
        r2 = separar_silabas("constitución")
        self.assertEqual(len(r1), 4)
        self.assertEqual(len(r2), 4)

    # v + c + c + c + v
    # Pero, si la tercera consonante es "l" o "r" , se separa la primera en una sílaba y las dos siguientes en otra.
    def test_7(self):
        r1 = separar_silabas("entrega")
        r2 = separar_silabas("espronceda")
        self.assertEqual(len(r1), 3)
        self.assertEqual(len(r2), 4)

    # v + c + c + c + c + v
    # Cuando tienes cuatro consonantes, las dos primeras forman una sílaba y las dos siguientes otra.
    def test_8(self):
        r1 = separar_silabas("transgredir")
        r2 = separar_silabas("instrucción")
        self.assertEqual(len(r1), 3)
        self.assertEqual(len(r2), 3)

    # consonante doble
    # Las letras rr, ll y ch forman un solo sonido. No se separan.
    def test_9(self):
        r1 = separar_silabas("llevar")
        r2 = separar_silabas("carretera")
        r3 = separar_silabas("perro")
        r4 = separar_silabas("chicharron")
        self.assertEqual(len(r1), 2)
        self.assertEqual(len(r2), 4)
        self.assertEqual(len(r3), 2)
        self.assertEqual(len(r4), 3)

    # h
    # La h sigue las mismas reglas anteriores y cuenta como consonante, 
    # a excepción de los diptongos y hiatos que estudiaremos a continuación.
    def test_10(self):
        r1 = separar_silabas("adherir")
        r2 = separar_silabas("hembra")
        self.assertEqual(len(r1), 3)
        self.assertEqual(len(r2), 2)
    
    # qu
    # Nunca se separa la qu.
    def test_11(self):
        r1 = separar_silabas("querida")
        r2 = separar_silabas("alquimista")
        self.assertEqual(len(r1), 3)
        self.assertEqual(len(r2), 4)

    def test_versometro_medir_verso(self):
        r1 = medir_verso("Amor, no te llame amor")        
        self.assertEqual(r1[0], 8)

    def test_versometro_medir_poema(self):
        poema =    ["Amor, no te llame amor", 
                    "el que no te corresponde", 
                    "pues que no hay materia adonde", 
                    "imprima forma el favor.", 
                    "naturaleza, en rigor,",
                    "conservó tantas edades",
                    "correspondiendo amistades",
                    "que no hay animal perfecto",
                    "si no asiste a su concepto",
                    "la unión de dos voluntades"]
    
        for verso in poema:
            medir_verso(verso)
