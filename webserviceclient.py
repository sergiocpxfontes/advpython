import requests
import logging

logging.basicConfig(filename="militarapp.log",format='%(asctime)s %(message)s',level=logging.INFO)

Headers = { "Token" : "W74644#$","App":"3423"}

# consulta webservice lista
url = "http://127.0.0.1:5000/webservice"
logging.info(url)
resultado = ""
try:
    resposta = requests.get(url,headers=Headers)
    resultado = resposta.json()
    print(resultado)
    logging.debug(resultado)
except Exception as e:
    logging.critical(e)




# consulta webservice detalhe
url = "http://127.0.0.1:5000/webservice/4578"
logging.info(url)
try:
    resposta = requests.get(url,headers=Headers)
    print(resposta.json())
except Exception as e:
    logging.critical(e)

# post webservice
url = "http://127.0.0.1:5000/webservicepost"
logging.info(url)
paylod=[{"CC": "Antonio", "Nome": "Antonio", "Apelido": "Silva", "NIF": "45678", "DataNascimento": "12-12-1986", "NIM": "4578", "Patente": "General", "Ramo": ""}, {"CC": "", "Nome": "", "Apelido": "", "NIF": "", "DataNascimento": "12-12-1986", "NIM": "", "Patente": "", "Ramo": ""}, {"CC": "1234", "Nome": "Mario", "Apelido": "Jos\u00e9", "NIF": "45678", "DataNascimento": "12-12-1986", "NIM": "4579", "Patente": "General", "Ramo": ""}, {"CC": "2345", "Nome": "Maria", "Apelido": "Antunes", "NIF": "45678", "DataNascimento": "12-12-1986", "NIM": "4580", "Patente": "General", "Ramo": ""}, {"CC": "3456", "Nome": "Jos\u00e9", "Apelido": "Janu\u00e1rio", "NIF": "45678", "DataNascimento": "12-12-1986", "NIM": "4581", "Patente": "General", "Ramo": ""}, {"CC": "4567", "Nome": "Marco", "Apelido": "Antunes", "NIF": "45678", "DataNascimento": "12-12-1986", "NIM": "4582", "Patente": "General", "Ramo": ""}, {"CC": "5678", "Nome": "Anda", "Apelido": "Silva", "NIF": "45678", "DataNascimento": "12-12-1986", "NIM": "4583", "Patente": "General", "Ramo": ""}]
resposta = requests.post(url,json=paylod,headers=Headers)
print(resposta.json())