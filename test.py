import unittest
import logging

from repentista.silabeador import separar_silabas
from repentista.metrica import medir_verso
from repentista.acentuacion import silaba_tonica, tipo_palabra, ultima_vocal_tonica, TipoAcentuacion
from repentista.rima import rima_verso, rima_poema, TipoRima

def setUpModule():
    logging.basicConfig(level=logging.DEBUG)


class TestSilabrador(unittest.TestCase):
    
    # c + v : 
    # Las consonantes solas no forman sílabas
    def test_2(self): 
        r0 = separar_silabas("corría")
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

    def test_12_hiatos(self):
        r = separar_silabas("Dúo")
        self.assertEqual(len(r), 2)
        r = separar_silabas("Encía")
        self.assertEqual(len(r), 3)
        r = separar_silabas("Insinúe")
        self.assertEqual(len(r), 4)
        r = separar_silabas("Sonríe")
        self.assertEqual(len(r), 3)
        r = separar_silabas("Bahía")
        self.assertEqual(len(r), 3)
        r = separar_silabas("Vehículo")
        self.assertEqual(len(r), 4)
        r = separar_silabas("Deseo")
        self.assertEqual(len(r), 3)
        r = separar_silabas("Aéreo")
        self.assertEqual(len(r), 4)
        r = separar_silabas("Canoa")
        self.assertEqual(len(r), 3)
        r = separar_silabas("Alcohol")
        self.assertEqual(len(r), 3)
        r = separar_silabas("Creer")
        self.assertEqual(len(r), 2)
        r = separar_silabas("Leer")
        self.assertEqual(len(r), 2)
        r = separar_silabas("Cooperar")
        self.assertEqual(len(r), 4)
        r = separar_silabas("Azahar")
        self.assertEqual(len(r), 3)

class TestMetrica(unittest.TestCase):
    def test_medir_verso(self):
        r = medir_verso("Amor, no te llame amor")        
        self.assertEqual(r['medida'], 8)

    def test_medir_poema(self):
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

    def test_medir_poema_2(self):
        poema =    ["Se va con algo mío la tarde que se aleja...", 
                    "mi dolor de vivir es un dolor de amar,", 
                    "y al son de la garúa, en la antigua calleja,", 
                    "me invade un infinito deseo de llorar.", 
                    "Que son cosas de niño me dices... ¡Quién me diera,",
                    "tener una perenne inconciencia infantil,",
                    "ser del reino del día y de la primavera,",
                    "del ruiseñor que canta y del alba de abril!",
                    "¡Ah, ser pueril, ser puro, ser canoro, ser suave",
                    "trino, perfume o canto, crepúsculo o aurora;",
                    "como la flor que aroma la vida… y no lo sabe,",
                    "como el astro que alumbra las noches… y lo ignora! "]
    
        for verso in poema:
            medir_verso(verso)

    def test_licencias(self):
        r = medir_verso("Juana estaba acostada")        
        self.assertEqual(r['medida'], 7)
        r = medir_verso("Cantando allá va María")        
        self.assertEqual(r['medida'], 7)
        r = medir_verso("José, solo con el abrigo y los guantes es suficiente")        
        self.assertEqual(r['medida'], 17)
        r = medir_verso("María y el amigo")        
        self.assertEqual(r['medida'], 5)
        r = medir_verso("La paz y la humanidad deben ir de la mano")        
        self.assertEqual(r['medida'], 14)
        r = medir_verso("El camión llevaba láminas de zinc y hierro")       
        self.assertEqual(r['medida'], 14)
        r = medir_verso("María andaba jugando a las diez")        
        self.assertEqual(r['medida'], 10)

class TestAcentuador(unittest.TestCase):
    def test_silaba_tonica(self):
        r = silaba_tonica("revolución")
        self.assertEqual(r[1], 4)
        r = silaba_tonica("revés")
        self.assertEqual(r[1], 2)
        r = silaba_tonica("panel")
        self.assertEqual(r[1], 2)
        r = silaba_tonica("lápiz")
        self.assertEqual(r[1], 1)
        r = silaba_tonica("esdrújula")
        self.assertEqual(r[1], 2)
        r = silaba_tonica("cantándoselas")
        self.assertEqual(r[1], 2)

    def test_tipo_palabra(self):
        r = tipo_palabra("revolución")
        self.assertEqual(r, TipoAcentuacion.AGUDA)
        r = tipo_palabra("revés")
        self.assertEqual(r, TipoAcentuacion.AGUDA)
        r = tipo_palabra("panel")
        self.assertEqual(r, TipoAcentuacion.AGUDA)
        r = tipo_palabra("lápiz")
        self.assertEqual(r, TipoAcentuacion.LLANA)
        r = tipo_palabra("pena")
        self.assertEqual(r, TipoAcentuacion.LLANA)
        r = tipo_palabra("esdrújula")
        self.assertEqual(r, TipoAcentuacion.ESDRUJULA)
        r = tipo_palabra("cántame")
        self.assertEqual(r, TipoAcentuacion.ESDRUJULA)
        r = tipo_palabra("cantándoselas")
        self.assertEqual(r, TipoAcentuacion.SOBRE_ESDRUJULA)
        r = tipo_palabra("la")
        self.assertEqual(r, TipoAcentuacion.MONOSILABA)

    def test_ultima_vocal_tonica(self):
        r = ultima_vocal_tonica("cifra")
        self.assertEqual(r, 2)
        r = ultima_vocal_tonica("revolución")
        self.assertEqual(r, 9)
        r = ultima_vocal_tonica("revés")
        self.assertEqual(r, 4)
        r = ultima_vocal_tonica("panel")
        self.assertEqual(r, 4)
        r = ultima_vocal_tonica("lápiz")
        self.assertEqual(r, 2)
        r = ultima_vocal_tonica("pena")
        self.assertEqual(r, 2)
        r = ultima_vocal_tonica("esdrújula")
        self.assertEqual(r, 5)
        r = ultima_vocal_tonica("cántame")
        self.assertEqual(r, 2)
        r = ultima_vocal_tonica("cantándoselas")
        self.assertEqual(r, 5)
        r = ultima_vocal_tonica("la")
        self.assertEqual(r, 2)

class TestRima(unittest.TestCase):
    def test_rima(self):
        self.assertEqual(rima_verso("Mi niña llegó riendo","a quien yo sigo queriendo."), TipoRima.CONSONATE)
        self.assertEqual(rima_verso("por el hogar que creamos","se respira que la amamos"), TipoRima.CONSONATE)
        self.assertEqual(rima_verso("en una caja a mi vida","como su mamá querida"), TipoRima.CONSONATE)

    def test_rima_poema(self):
        poema =    ["Yo capturo aquel momento", 
                    "en que el mundo nos ignora", 
                    "y en nuestro universo aflora", 
                    "un beso con sentimiento.", 
                    "Del beso tengo tu aliento",
                    "y de tu boca el sabor",
                    "y mientras corre el rumor",
                    "de las olas vespertinas",
                    "capturo de tus retinas",
                    "ese momento de amor."]
        rima = rima_poema(poema)
        self.assertEqual(rima, ['a', 'b', 'b', 'a', 'a', 'c', 'c', 'd', 'd', 'c'])