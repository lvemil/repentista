import csv
import json
import sqlite3
from sqlite3 import Error

from repentista.rima import ultima_vocal_tonica

def cargar_palabras(archivo):
    with open(archivo) as a:
        palabras = [fila.rstrip('\n') for fila in a]
        return palabras

def separar_ultima_vocal_tonica(palabras):
    separadas = []
    for palabra in palabras:
        try:
            vocal = ultima_vocal_tonica(palabra)
            terminacion = palabra[vocal-1:]
            inicio = palabra[:vocal-1]
            separadas.append((inicio, terminacion))
        except:
            print(f"{palabra} no pudo procesarse")
    return separadas

def separar_ultima_vocal_tonica_2(palabras):
    separadas = {}
    for palabra in palabras:
        try:
            vocal = ultima_vocal_tonica(palabra)
            terminacion = palabra[vocal-1:]
            inicio = palabra[:vocal-1]
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

def guardar_palabras_json(palabras, archivo):
    with open(archivo, 'w') as a:
        json.dump(palabras, a)

def guardar_palabras_db(palabras, db):
    try:
        con = sqlite3.connect(db)
        cur = con.cursor()
        cur.execute("CREATE TABLE palabras(terminacion text, palabras text)")
        for k in palabras:
            ps = ",".join([p for p in palabras[k] if p])
            sql = f"INSERT INTO palabras VALUES ('{k}','{ps}')"
            cur.execute(sql)
        con.commit()
    except Error as e:
        print(e)
    finally:
        con.close()

if __name__ == "__main__":
    palabras = cargar_palabras("data/formas.txt")
    separadas = separar_ultima_vocal_tonica_2(palabras)
    guardar_palabras_db(separadas, "data/palabras.db")