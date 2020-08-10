import sqlite3
from sqlite3 import Error

class Poema:
    
    def __init__(self, titulo = "", cuerpo = "", fecha = ""):
        self.titulo = titulo
        self.cuerpo = cuerpo

    @staticmethod
    def ObtenerTodos(db):
        try:
            con = sqlite3.connect(db)
            cur = con.cursor()
            sql = f"SELECT * FROM poema"
            cur.execute(sql)
            poemas = cur.fetchall()
            return poemas
        except Error as e:
            print(e)
        finally:
            con.close()

    @staticmethod
    def Obtener(id):
        pass

    @staticmethod
    def Guardar(poema):
        pass

