import logging

from repentista.silabeador import separar_silabas

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    poema = ["Amor, no te llame amor", 
        "el que no te corresponde", 
        "pues que no hay materia adonde", 
        "imprima forma el favor.", 
        "naturaleza, en rigor,",
        "conservó tantas edades",
        "correspondiendo amistades",
        "que no hay animal perfecto",
        "si no asiste a su concepto",
        "la unión de dos voluntades"]
    
    palabras = verso.lower().split(" ")
    for palabra in palabras:
        silabas = separar_silabas(palabra)