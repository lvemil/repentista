import logging
import re
from enum import Enum

from repentista.silabeador import separar_silabas

class TipoAcentuacion(Enum):
    AGUDA = 1
    LLANA = 2
    ESDRUJULA = 3
    SOBRE_ESDRUJULA = 4
    MONOSILABA = 5

def silaba_tonica(palabra):
    # separar la palabra en silabas
    silabas = separar_silabas(palabra)    
    if len(silabas) == 1: # monosilaba
        return silabas, 1
    # buscar silaba con tilde
    for i in range(len(silabas)):
        silaba = silabas[i]
        if re.findall("[áéíóú]", silaba): # la silaba tiene tilde
            return silabas, i+1
    # la palabra no tiene tilde
    if re.findall("[nsaeiou]$", palabra): # palabra termina en n,s o vocal
        return silabas, len(silabas) - 1 # palabra llana
    else:
         return silabas, len(silabas) # palabra aguda

def tipo_palabra(palabra):
    r = silaba_tonica(palabra)
    if len(r[0]) == 1:
        return TipoAcentuacion.MONOSILABA
    else:
        s = len(r[0]) - r[1]
        if s == 0:
            return TipoAcentuacion.AGUDA
        elif s == 1:
            return TipoAcentuacion.LLANA
        elif s == 2:
            return TipoAcentuacion.ESDRUJULA
        else:
            return TipoAcentuacion.SOBRE_ESDRUJULA

def ultima_vocal_tonica(palabra):
    silabas, no = silaba_tonica(palabra)
    silaba = silabas[no-1]
    
    for i in range(len(silaba)-1, -1, -1):
        if silaba[i] in "[aeiouáéíóú]":
            indice = len(palabra) - (len(silaba) - i + sum([len(s) for s in silabas[no:]])) + 1
            return indice

def separar_vocal_tonica(palabra):
    vocal = ultima_vocal_tonica(palabra)
    terminacion = palabra[vocal-1:]
    inicio = palabra[:vocal-1]
    return inicio, terminacion