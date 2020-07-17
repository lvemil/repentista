import logging
import string
import re

from repentista import silabeador

# sinalefa, sineresis, 
def es_licencia(silaba1, silaba2):
    if re.findall("[aeiouáéíóúy]$", silaba1): # silaba1 termina en vocal
        if silaba2.startswith('h'): # la h no impide la sinalefa
            silaba2 = silaba2[1:]
            if silaba2[0:2] in ["ie", "ia", "ui", "ue"]: # excepciones respecto a la h
                return False
        if re.findall("^[aeiouáéíóúy]", silaba2):
            return True
    return False

def medir_verso(verso):
    verso = verso.translate(str.maketrans('', '', string.punctuation))
    palabras = verso.split(" ")
    silabas_todas = []
    for palabra in palabras:
        silabas = silabeador.separar_silabas(palabra)
        silabas_todas += silabas
    
    # identificar licencias (sinalefa, sineresis)
    metrica = [silabas_todas[0]]
    for i in range(1, len(silabas_todas)):
        silaba1 = metrica[-1]
        silaba2 = silabas_todas[i]
        if es_licencia(silaba1, silaba2):
            metrica[-1] = f"{silaba1} {silaba2}"
        else:
            metrica.append(silaba2)

    # sumar o restar segun la clasificacion de la ultima palabra

    logging.debug(f"\n {'/ '.join(metrica)}")
    return metrica
