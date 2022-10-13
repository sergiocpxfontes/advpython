
from parameterized import parameterized, parameterized_class
import unittest
from militar_app.utilscls import Utils
from militar_app.militarcls import Militar
def soma(x,y):
    return x + y

class Tests(unittest.TestCase):
    @unittest.skip("razao para nao executar o teste")
    def test_soma(self):
        self.assertEqual(soma(5,5),10)

    @parameterized.expand([(5,10),(10,20),(20,40)])
    def test_soma1(self,input,expect):
        self.assertEqual(soma(input,input),expect)

    def test_DeleteMilitar(self):
        if Militar.Eliminar("9000"):
            obj=Militar()
            obj.Get("9000")
            self.assertNotEqual(obj.NIM,"9000")
        else:
            self.assertFalse(1==2)


    def test_InsertMilitar(self):
        obj0 = Militar()
        obj0.NIM="9000"
        obj0.CC="123456789"
        obj0.NIF="123456789"
        obj0.Nome="Ana"
        obj0.Apelido="Antunes"
        obj0.DataNascimento="25-08-1976"
        obj0.Patente="Coronel"
        obj0.Ramo="Marinha"

        if obj0.Inserir():
            obj1 = Militar()
            obj1.Get("9000")
            self.assertDictEqual(obj0.ToDictionary(),obj1.ToDictionary())

        else:
            self.assertFalse(1==2)
        


    def test_dictio(self):
        valorinicial = "{ \"nome\":\"Maria\", \"apelido\":\"Silva\"}" 
        valoresperado = {"nome":"Antonio","apelido":"Silva"}
        valorresutado =Utils.ImpostarJSON(valorinicial)
        self.assertDictEqual(valoresperado,valorresutado)


print('oi')


if __name__=='__main__':
    unittest.main()