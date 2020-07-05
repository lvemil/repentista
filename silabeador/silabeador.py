import logging

def es_grupo_consonantico(consonante1, consonante2):
    consonante_licuante = "bcdfgpt"
    consonante_liquida = "lr"
    return consonante1 in consonante_licuante and consonante2 in consonante_liquida

def es_hiato(vocal1, vocal2):
    vocal_abierta = "aeoáéó"
    vocal_cerrada = "iuíú"
    vocal_acentuada = "áéíóú"
    return ((vocal1 in vocal_abierta and vocal2 in vocal_cerrada) or  # vocal abierta (a,e,o) + vocal cerrada(i,u)
            (vocal1 in vocal_abierta and vocal2 in vocal_abierta) or  # vocal abierta + vocal abierta
            (vocal1 not in vocal_acentuada and vocal2 not in vocal_acentuada) or # vocal no acentuada + misma vocal no acentuada
            (vocal1 in vocal_cerrada and vocal2 in vocal_cerrada and (vocal1 in vocal_acentuada or vocal2 in vocal_acentuada))) # vocal cerrada + vocal cerrada (alguna de ellas, acentuada)

def es_vocal(letra):
    vocales = "aeiouáéíóú"
    return letra in vocales

def es_consonante(letra):
    return not es_vocal(letra)

def es_letra_doble(letra, siguiente_letra):
    return letra + siguiente_letra in ["ch", "rr", "ll", "qu"]

def separar_silabas(palabra):
    silabas = []
    silaba = ""
    indice = 0
    while indice < len(palabra):
        letra = palabra[indice]
        if indice == len(palabra) - 1: # ultima letra
            silaba += letra
            silabas.append(silaba)
        else:
            siguiente_letra = palabra[indice+1]
            if es_vocal(letra): # vocal
                if es_hiato(letra, siguiente_letra):
                    silaba += letra
                    silabas.append(silaba)
                    silaba = ""
                else:
                    silaba += letra
            else: # consonante
                if es_letra_doble(letra, siguiente_letra): # ll, rr, ch, qu:
                        silaba += letra
                        silaba += palabra[indice+1]
                        silaba += palabra[indice+2]
                        silabas.append(silaba)
                        silaba = ""
                        indice += 3
                        continue  
                if es_consonante(siguiente_letra): # la siguiente letra es una consonante                     
                    if es_grupo_consonantico(letra, siguiente_letra):
                        silabas.append(silaba)
                        silaba = ""
                    else:
                        silaba += letra
                        silabas.append(silaba)
                        silaba = ""
                else: # la siguiente letra es una vocal
                    if silaba != "":
                        silabas.append(silaba)
                        silaba = ""
                    silaba += letra
        indice += 1     
    logging.debug(silabas)
    return silabas

