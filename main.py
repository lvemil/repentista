import logging

from silabeador.silabeador import separar_silabas

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    verso = "Cuentan de un sabio que un día la leona"
    palabras = verso.lower().split(" ")
    for palabra in palabras:
        silabas = separar_silabas(palabra)