def es_grupo_consonantico(consonante1, consonante2):
    consonante_licuante = "bcdfgpt"
    consonante_liquida = "lr"
    return consonante1 in consonante_licuante and consonante2 in consonante_liquida

def es_hiato(vocal1, vocal2):
    vocal_abierta = "iuíú"
    vocal_cerrada = "aeoáéó"
    return (vocal1 in vocal_abierta and vocal2 in vocal_cerrada) or (vocal2 in vocal_abierta and vocal1 in vocal_cerrada)

def es_vocal(letra):
    vocales = "aeiouáéíóú"
    return letra in vocales

def es_consonante(letra):
    return not es_vocal(letra)

def separar_silabas(palabra):
    silabas = []
    silaba = ""
    for indice in range(len(palabra)):
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
                if es_consonante(siguiente_letra): # la siguiente letra es una consonante
                    if es_grupo_consonantico(letra, siguiente_letra):
                        silabas += silaba
                        silaba = ""
                    else:
                        silaba += letra
                        silabas.append(silaba)
                        silaba = ""
                else: # la siguiente letra es una vocal
                    silaba += letra
    return silabas

if __name__ == "__main__":
    verso = "Cuentan de un sabio que un día"
    palabras = verso.lower().split(" ")
    for palabra in palabras:
        silabas = separar_silabas(palabra)
        print(silabas)