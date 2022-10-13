class Individuo():
    def __init__(self,cc="",nome="",apelido="",nif=""):
        self.CC = cc
        self.Nome = nome
        self.Apelido = apelido
        self.NIF = nif
        self.DataNascimento = "12-12-1986"


    def NomeCompleto(self):
        return self.Nome + " " + self.Apelido

    def Imprimir(self):
        print(self.NomeCompleto())