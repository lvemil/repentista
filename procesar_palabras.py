import csv
import zipfile
import sqlite3
import re
from sqlite3 import Error

from repentista.acentuacion import ultima_vocal_tonica, separar_vocal_tonica

def cargar_palabras(archivo):
    with open(archivo) as a:
        palabras = [fila.rstrip('\n') for fila in a]
        return palabras

def separar_ultima_vocal_tonica(palabras):
    separadas = []
    for palabra in palabras:
        try:
            inicio, terminacion = separar_vocal_tonica(palabra)
            separadas.append((inicio, terminacion))
        except:
            print(f"{palabra} no pudo procesarse")
    return separadas

def separar_ultima_vocal_tonica_2(palabras):
    separadas = {}
    for palabra in palabras:
        try:
            inicio, terminacion = separar_vocal_tonica(palabra)
            if terminacion in separadas:
                separadas[terminacion].append(inicio)
            else:
                separadas[terminacion] = [inicio]
        except:
            print(f"{palabra} no pudo procesarse")
    return separadas

def guardar_palabras_archivo(palabras, archivo):
    with open(archivo,'w') as out:
        w = csv.writer(out)
        w.writerows(palabras)

def guardar_palabras_db(palabras, db):
    try:
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute("CREATE TABLE palabras(terminacion text, vocales text, palabras text)")
        for k in palabras:
            vocales = "".join(re.findall("[aeiouáéíóú]", k))
            ps = ",".join([p for p in palabras[k] if p])
            sql = f"INSERT INTO palabras VALUES ('{k}','{vocales}','{ps}')"
            cur.execute(sql)
        con.commit()
    except Error as e:
        print(e)
    finally:
        con.close()

def comprimir(db):
    with zipfile.ZipFile(f"{db}.zip", mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(db, db.split('/')[-1])

if __name__ == "__main__":
    palabras = cargar_palabras("data/formas.txt")
    separadas = separar_ultima_vocal_tonica_2(palabras)
    guardar_palabras_db(separadas, "data/palabras.db")
    comprimir("data/palabras.db")