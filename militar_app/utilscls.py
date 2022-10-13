import csv
import json
from datetime import datetime
import sqlite3
from sqlite3 import Error

class Utils():
    CAMINHODB = "D:\\Projects\\Rumos\\Python_102022\\web\\militar_app\\militar.db"
    @staticmethod
    def SelectSQL(sql):
        lista = []
        conn = None
        try:
            conn = sqlite3.connect(Utils.CAMINHODB)
            c = conn.cursor()
            c.execute(sql)
            for row in c.fetchall():
                lista.append(row)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
        return lista
    @staticmethod
    def ExecuteSQL(sql):
        result=False
        conn = None
        try:
            conn = sqlite3.connect(Utils.CAMINHODB)
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
            result=True
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
        return result
    @staticmethod
    def ExportarCSV(ficheiro,titulos,registos, separador = ";"):
        try:
            #with open(ficheiro,"w",newline="") as ficheiroCSV:
            with open(ficheiro,"w") as ficheiroCSV:
                escrever = csv.DictWriter(ficheiroCSV,titulos
                ,delimiter=separador,quoting=csv.QUOTE_NONNUMERIC)
                escrever.writeheader()
                escrever.writerows(registos)
            return True
        except Exception as ex:
            print(ex)
            return False
    @staticmethod
    def ImportarCSV(ficheiro,separador=";"):
        lista =[]
        try:
            with open(ficheiro,"r") as ficheiroCSV:
                ler = csv.DictReader(ficheiroCSV,delimiter=separador)
                for linha in ler:
                    lista.append(linha)
                return True,lista
        except:
            print("erro")
            return False,lista


    @staticmethod
    def ExportarJSON(object):
        return json.dumps(object)

    @staticmethod
    def ImpostarJSON(value):
        return json.loads(value)

    @staticmethod
    def DataDif(datainicio,datafim,formato="D"):

        #idiomatic python
        if formato not in {"Y","M","D"}:
            return None

        di=datetime.strptime(datainicio,"%Y-%m-%d")
        df=datetime.strptime(datafim,"%Y-%m-%d")

        if formato=="D":
            dif = (df-di).days
        elif formato=="M":
            dif = (df-di).days /365/12
        elif formato=="Y":
            dif = (df-di).days /365
        return dif