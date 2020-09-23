configuracion = {"db":"data/repentista.db"}

class Configuracion:
    @staticmethod
    def obtener(key):
        return configuracion[key]