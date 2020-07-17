import logging
import string
import re

from repentista import silabeador
from repentista import acentuacion

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
    res = {}
    # medir verso
    verso = verso.translate(str.maketrans('', '', '¡!"#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}~'))
    palabras = verso.split(" ")
    silabas_gramaticales = []
    for palabra in palabras:
        silabas = silabeador.separar_silabas(palabra)
        silabas_gramaticales += silabas
    res["silabas_gramaticales"] = silabas_gramaticales
    
    # identificar licencias (sinalefa, sineresis)
    res["licencias"] = []
    silabas_metricas = [silabas_gramaticales[0]]
    for i in range(1, len(silabas_gramaticales)):
        silaba1 = silabas_metricas[-1]
        silaba2 = silabas_gramaticales[i]
        if es_licencia(silaba1, silaba2):
            ns = f"{silaba1} {silaba2}"
            res["licencias"].append(ns)
            silabas_metricas[-1] = ns
        else:
            silabas_metricas.append(silaba2)
    res["silabas_metricas"] = silabas_metricas
    medida = len(silabas_metricas)

    # sumar o restar segun la clasificacion de la ultima palabra
    tipo = acentuacion.tipo_palabra(palabras[-1])
    acento_ultima_palabra = 0
    if tipo == acentuacion.TipoAcentuacion.AGUDA or tipo == acentuacion.TipoAcentuacion.MONOSILABA:
        acento_ultima_palabra = 1
    elif tipo == acentuacion.TipoAcentuacion.ESDRUJULA:
        acento_ultima_palabra = -1
    medida += acento_ultima_palabra
    res["medida"] = medida
    res["acento_ultima_palabra"] = acento_ultima_palabra

    logging.debug(f"{'/ '.join(silabas_metricas)} {medida} {acento_ultima_palabra}")
    return res
