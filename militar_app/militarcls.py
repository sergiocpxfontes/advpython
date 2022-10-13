from militar_app.individuocls import Individuo
from militar_app.utilscls import Utils
class Militar(Individuo):
    def __init__(self,nim="",patente="", cc="", nome="", apelido="", nif=""):
        #super()).__init__(cc, nome, apelido, nif)
        Individuo.__init__(self,cc, nome, apelido, nif)
      
        self.NIM=nim
        self.Patente=patente
        self.Ramo =""
    def NomeCompleto(self):
        return self.NIM + " - " + self.Patente + " "  +self.Nome + " " + self.Apelido

    def ToDictionary(self):
        return self.__dict__
    
    def ToList(self):
        return list(self.__dict__.values())

    def Get(self,nim):
        sql ="SELECT * FROM militares WHERE NIM='{0}'"
        sql = sql.format(nim)
        for row in Utils.SelectSQL(sql):
            self.NIM = str(row[0])
            self.Patente = str(row[1])
            self.CC= str(row[2])
            self.Nome = str(row[3])
            self.Apelido = str(row[4])
            self.NIF = str(row[5])
            self.DataNascimento = str(row[6])
            self.Ramo = str(row[7])
    def Inserir(self):
        sql = """INSERT INTO militares (NIM,Patente,CC,Nome,Apelido,NIf,DataNascimento,Ramo) 
        values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')"""

        sql = sql.format(self.NIM,self.Patente,self.CC,self.Nome,self.Apelido,self.NIF,self.DataNascimento,self.Ramo)
        print(sql)
        return Utils.ExecuteSQL(sql)
    def Atualizar(self):
        sql = """UPDATE militares SET Patente='{1}',CC='{2}',Nome='{3}',Apelido='{4}'
        ,NIf='{5}',DataNascimento='{6}',Ramo='{7}' WHERE NIM='{0}'"""

        sql = sql.format(self.NIM,self.Patente,self.CC,self.Nome,self.Apelido,self.NIF,self.DataNascimento,self.Ramo)
        return Utils.ExecuteSQL(sql)

    @staticmethod
    def Eliminar(value):
        sql ="DELETE FROM militares WHERE NIM='{0}'"
        sql = sql.format(value)
        return Utils.ExecuteSQL(sql)
    @staticmethod
    def ListaRegistos():
        lista =[]
        sql = "SELECT * FROM militares"
        for row in Utils.SelectSQL(sql):
            #print(row)
            militar = Militar()
            militar.NIM = str(row[0])
            militar.Patente = str(row[1])
            militar.CC= str(row[2])
            militar.Nome = str(row[3])
            militar.Apelido = str(row[4])
            militar.NIF = str(row[5])
            militar.DataNascimento = str(row[6])
            militar.Ramo = str(row[7])
            lista.append(militar)
        return lista
    @staticmethod
    def ExportarParaCSV(ficheiro,registos,separador=";"):
        #titulos = list(Militar.__dict__.keys())
        titulos = ["NIM","Patente","CC","Nome","Apelido","NIF","DataNascimento","Ramo"]
        print(titulos)
        return Utils.ExportarCSV(ficheiro,titulos,registos,separador)

    @staticmethod
    def ImportarDeCSV(ficheiro,separador=";"):
        lst =[]
        titulos = ["NIM","Patente","CC","Nome","Apelido","NIF","DataNascimento","Ramo"]
        (resultado,lista)=Utils.ImportarCSV(ficheiro)
        if resultado:
            for linha in lista:
                militar = Militar()
                for key in linha.keys():
                    for ckey in list(titulos):
                        if key== ckey:
                            militar.__dict__[ckey]=linha[key]
                lst.append(militar)
        return lst

    @staticmethod
    def ImportarDeJSON(lista):
        lst =[]
        titulos = ["NIM","Patente","CC","Nome","Apelido","NIF","DataNascimento","Ramo"]
        for linha in lista:
            militar = Militar()
            for key in linha.keys():
                for ckey in list(titulos):
                    if key== ckey:
                        militar.__dict__[ckey]=linha[key]
            lst.append(militar)
        return lst
