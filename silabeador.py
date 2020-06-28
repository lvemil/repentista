def es_grupo_consonantico(consonante1, consonante2):
    consonante_licuante = "bcdfgpt"
    consonante_liquida = "lr"
    return consonante1 in consonante_licuante and consonante2 in consonante_liquida

def es_vocal(letra):
    vocales = "aeiouáéíóú"
    return letra in vocales

def es_consonante(letra):
    return not es_vocal(letra)

def separar_silabas(palabra):
    silabas = []
    silaba = ""
    for indice in range(palabra):
        letra = palabra[indice]
        if es_vocal(letra):
            silaba += letra
        else: # consonante
            if indice == len(palabra) - 1: # ultima letra
                silaba += letra
                silabas =+ silaba
            else:
                siguiente_letra = palabra[indice+1]
                if es_consonante(siguiente_letra): # la siguiente letra es una consonante
                    if es_grupo_consonantico(letra, siguiente_letra):
                        silabas += silaba
                        silaba = ""
                    else:
                        silaba += letra
                        silabas += silaba
                        silaba = ""
                else: # la siguiente letra es una vocal
                    



    return silabas

if __name__ == "__main__":
    verso = "Cuentan de un sabio que un día"
    palabras = verso.lower().split(" ")
    for palabra in palabras:
        silabas = separar_silabas(palabra)