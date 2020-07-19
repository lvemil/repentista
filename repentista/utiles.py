import string

def limpiar(verso):
    return verso.translate(str.maketrans('', '', '¡!"#$%&\'()*+,-./:;<=>¿?@[\\]^_`{|}~'))