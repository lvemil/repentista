from repentista.rima import TipoRima

def composicion(nombre = ""):
    """recibe el nombre de una composicion y retorna la rima esperada entre versos y el tipo de rima"""
    composiciones = {
        "pareado" : ([(0,"a"),(0,"a")], None),
        "alegria" : ([(5,"a"),(10,"a")], TipoRima.ASONANTE),
        "terceto" : ([(11,"a"),(11,""),(11,"A")], TipoRima.CONSONATE),
        "tercetillo" : ([(8,"a"),(8,""),(8,"a")], None),
        "solea" : ([(8,"a"),(8,""),(8,"a")], TipoRima.ASONANTE),
        "cuarteto" : ([(11,"a"),(11,"b"),(11,"b"),(11,"a")], TipoRima.CONSONATE),
        "redondilla" : ([(8,"a"),(8,"b"),(8,"b"),(8,"a")], TipoRima.CONSONATE),
        "serventesio" : ([(11,"a"),(11,"b"),(11,"a"),(11,"b")], TipoRima.CONSONATE),
        "cuarteta" : ([(8,"a"),(8,"b"),(8,"a"),(8,"b")], TipoRima.CONSONATE),
        "copla" : ([(0,""),(0,"a"),(0,""),(0,"a")], None),
        "seguidilla" : ([(7,""),(5,"a"),(7,""),(5,"a")], TipoRima.ASONANTE),
        "cuaderna_via" : ([(14,"a"),(14,"a"),(14,"a"),(14,"a")], None),
        "lira" : ([(7,"a"),(11,"b"),(7,"a"),(7,"b"),(11,"b")], None),
        "copla_manriquena" : ([(8,"a"),(8,"b"),(4,"c"),(8,"a"),(8,"b")], None),
        "octavilla" : ([(8,"-"),(8,"a"),(8,"a"),(8,"b"),(8,"-"),(8,"c"),(8,"c"),(8,"b")], None),
        "octava_real" : ([(11,"a"),(11,"b"),(11,"a"),(11,"b"),(11,"a"),(11,"b"),(11,"c"),(11,"c")], None),
        "copla_arte_mayor" : ([(12,"a"),(12,"b"),(12,"b"),(12,"a"),(12,"a"),(12,"c"),(12,"c"),(12,"a")], TipoRima.CONSONATE),
        "decima" : ([(8,"a"),(8,"b"),(8,"b"),(8,"a"),(8,"a"),(8,"c"),(8,"c"),(8,"d"),(8,"d"),(8,"c")], None),
        "copla_real" : ([(8,"a"),(8,"b"),(8,"a"),(8,"a"),(8,"b"),(8,"c"),(8,"d"),(8,"c"),(8,"c"),(8,"d")], TipoRima.CONSONATE),
    }
    if nombre:
        if nombre in composiciones:
            return composiciones[nombre]
    else:
        return composiciones

def debe_rimar_con(verso, nombre_composicion):
    """retorna con que verso debe rimar el verso indicado para una composicion indicada"""
    c = composicion(nombre_composicion)
    versos = c[0]
    letra = versos[verso-1][1]
    e = list(enumerate([x[1] for x in versos]))
    v = [x for x in e if x[0]<verso-1 and x[1] == letra]
    if v:
        return v[-1][0]+1
    else:
        return None
