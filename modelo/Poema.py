import sqlite3
from sqlite3 import Error

class Poema:
    
    def __init__(self, id = "", titulo = "", cuerpo = "", modificado = ""):
        self.id = id
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.modificado = modificado

    @staticmethod
    def ObtenerTodos(db, orden = "DESC"):
        assert orden in ["DESC", "ASC"]
        try:
            con = sqlite3.connect(db)
            cur = con.cursor()
            sql = f"SELECT * FROM poema ORDER BY modificado {orden}"
            cur.execute(sql)
            poemas = cur.fetchall()
            return poemas
        except Error as e:
            print(e)
        finally:
            con.close()

    @staticmethod
    def Obtener(db, id):
        assert id
        try:
            con = sqlite3.connect(db)
            cur = con.cursor()
            sql = f"SELECT * FROM poema where id = '{id}'"
            cur.execute(sql)
            poemas = cur.fetchall()
            if poemas:
                p = Poema(poemas[0][0],poemas[0][1], poemas[0][2], poemas[0][3])
                return p
            else:
                return None            
        except Error as e:
            print(e)
        finally:
            con.close()

    @staticmethod
    def Guardar(poema):
        pass
