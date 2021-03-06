import sqlite3
from sqlite3 import Error
import uuid
import datetime

class Poema:
    
    def __init__(self, id = "", titulo = "", composicion = "", cuerpo = "", modificado = ""):
        self.id = id
        self.titulo = titulo
        self.composicion = composicion
        self.cuerpo = cuerpo
        self.modificado = modificado

    @staticmethod
    def ObtenerTodos(db, orden = "DESC", eliminados = False):
        assert orden in ["DESC", "ASC"]
        try:
            con = sqlite3.connect(db)
            cur = con.cursor()
            if eliminados:
                sql = f"SELECT * FROM poema ORDER BY modificado {orden}"
            else:
                sql = f"SELECT * FROM poema WHERE Eliminado = 0 ORDER BY modificado {orden}"
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
            sql = f"SELECT * FROM poema where id = ?"
            cur.execute(sql, [id])
            poemas = cur.fetchall()
            if poemas:
                p = Poema(id=poemas[0][0],titulo=poemas[0][1], composicion=poemas[0][5], cuerpo = poemas[0][2], modificado=poemas[0][3])
                return p
            else:
                return None            
        except Error as e:
            print(e)
        finally:
            con.close()

    @staticmethod
    def Guardar(db, poema):
        assert poema
        try:
            cuerpo = "\n".join(poema.cuerpo)     
            con = sqlite3.connect(db)
            cur = con.cursor()
            modificado = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if poema.id:
                sql = f"UPDATE poema SET Titulo = ?, Composicion = ?, Cuerpo = ?, Modificado = ? WHERE id = ?"
                cur.execute(sql, (poema.titulo, poema.composicion, cuerpo, modificado, poema.id))
            else:
                id = str(uuid.uuid1())                
                sql = f"INSERT INTO poema (ID, Titulo, Composicion, Cuerpo, Modificado, Eliminado) VALUES (?, ?, ?, ?, ?, 0)"
                cur.execute(sql, (id, poema.titulo, poema.composicion, cuerpo, modificado))
            
            con.commit()
            return poema.id if poema.id else id
        except Error as e:
            print(f"ERROR: {e}")
            return None
        finally:
            con.close()

    @staticmethod
    def Eliminar(db, id):
        assert id
        try:  
            con = sqlite3.connect(db)
            cur = con.cursor()
            sql = f"UPDATE poema SET Eliminado = 1 WHERE id = ?"
            cur.execute(sql, [id])            
            con.commit()
        except Error as e:
            print(e)
            return None
        finally:
            con.close()