import logging
import re
from enum import Enum

from repentista.silabeador import separar_silabas
from repentista.acentuacion import ultima_vocal_tonica
from repentista import utiles

class TipoRima(Enum):
    CONSONATE = 1
    ASONANTE = 2

def rima_palabra(palabra1, palabra2):
    vocal1 = ultima_vocal_tonica(palabra1)
    terminacion1 = palabra1[vocal1-1:]

    vocal2 = ultima_vocal_tonica(palabra2)
    terminacion2 = palabra2[vocal2-1:]

    if terminacion1 == terminacion2:
        return TipoRima.CONSONATE
    else:
        t1 = "".join(re.findall("[aeiouáéíóú]", terminacion1))
        t2 = "".join(re.findall("[aeiouáéíóú]", terminacion2))
        return t1 == t2

def rima_verso(verso1, verso2):   
    verso1 = utiles.limpiar(verso1)
    palabra1 = verso1.split(" ")[-1]
    
    verso2 = utiles.limpiar(verso2)
    palabra2 = verso2.split(" ")[-1]
    
    return rima_palabra(palabra1, palabra2)

def rima_poema(poema):
    rima = [None] * len(poema)
    letras = 'abcdefghijklmnopqrstuvwxyz'
    i_letra = 0
    for i in range(len(poema) - 1):
        if rima[i]:
            continue
        for j in range(i+1, len(poema), 1):
            if rima[j]:
                continue
            if rima_verso(poema[i], poema[j]):
                rima[i] = letras[i_letra]
                rima[j] = letras[i_letra]
        i_letra += 1
    return rima

            
            