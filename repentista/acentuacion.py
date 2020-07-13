import unittest
import logging
import re

from repentista.silabeador import separar_silabas

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

        

