import logging
import re
from enum import Enum
import sqlite3
from sqlite3 import Error

from repentista.silabeador import separar_silabas
from repentista.acentuacion import ultima_vocal_tonica, separar_vocal_tonica
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
        if t1 == t2:
            return TipoRima.ASONANTE
    return False

def rima_verso(verso1, verso2):   
    verso1 = utiles.limpiar(verso1)
    palabra1 = verso1.split(" ")[-1]
    
    verso2 = utiles.limpiar(verso2)
    palabra2 = verso2.split(" ")[-1]
    
    return rima_palabra(palabra1, palabra2)

def rima_poema(poema):
    if poema:
        if len(poema) == 1:
            return ["a"]
        else:
            rima = [""] * len(poema)
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
    else:
        return None

def riman_con(palabra,db):
    _,terminacion = separar_vocal_tonica(palabra)
    vocales = "".join(re.findall("[aeiouáéíóú]", terminacion))
    try:
        con = sqlite3.connect(db)
        cur = con.cursor()
        
        # buscar palabras con rima consonante
        sql = f"SELECT palabras FROM palabras WHERE terminacion = '{terminacion}'"
        cur.execute(sql)
        palabras = cur.fetchall()
        if palabras:
            consonante = [p + terminacion for p in palabras[0][0].split(",")]

        # buscar palabras con rima asonante
        sql = f"SELECT terminacion, palabras FROM palabras WHERE vocales = '{vocales}' AND terminacion <> '{terminacion}'"
        cur.execute(sql)
        palabras = cur.fetchall()
        asonante = []
        for r in palabras:
            asonante += [p + r[0] for p in r[1].split(",")]
        return consonante, asonante
    except Error as e:
        print(e)
    finally:
        con.close()
            