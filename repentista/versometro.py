import logging
import string

from repentista import silabeador

def medir_verso(verso):
    verso = verso.translate(str.maketrans('', '', string.punctuation))
    palabras = verso.split(" ")
    metrica = []
    medida = 0
    for palabra in palabras:
        silabas = silabeador.separar_silabas(palabra)
        metrica.append((palabra, silabas))
        medida += len(silabas)
    logging.debug(f"\n {'/ '.join([item for sublist in [x[1] for x in metrica] for item in sublist])} : {medida}")
    return medida, metrica
