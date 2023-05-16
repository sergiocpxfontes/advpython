import logging
from flask import Flask,render_template,redirect,url_for, request,jsonify
from militar_app.militarcls import Militar
from militar_app.utilscls import Utils
app = Flask(__name__)

logging.basicConfig(filename="militarapp.log",format='%(asctime)s %(message)s',level=logging.INFO)

@app.route("/")
def home():
    logging.info("Action home")
    return render_template(
        "home.html"
        ,valor="Sergio Fontes"
    )

@app.route("/militares")
def militares():
    logging.info("Action militares")
    lista = Militar.ListaRegistos()
    return render_template(
        "militares.html"
        ,militares=lista
    )

@app.route("/eliminar/<id>")
def eliminar(id):
    Militar.Eliminar(id)
    return redirect(url_for('militares'))

@app.route("/ver/<id>")
def ver(id):
    militar = Militar()
    militar.Get(id)
    return render_template(
        "detalhe.html"
        ,militar=militar
    )

@app.route("/editar/<id>")
def editar(id):
    militar = Militar()
    militar.Get(id)
    return render_template(
        "editar.html"
        ,militar=militar
    )


@app.route("/atualizar",methods = ['POST'])
def atualizar():
    if request.method == 'POST':
        nim =request.form ['nim']
        patente =request.form ['patente']
        cc =request.form ['cc']
        nome =request.form ['nome']
        apelido =request.form ['apelido']
        nif =request.form ['nif']
        ramo =request.form ['ramo']

        militar = Militar()
        militar.NIM = nim
        militar.Patente = patente
        militar.CC = cc
        militar.Nome = nome
        militar.Apelido = apelido
        militar.NIF = nif
        militar.Ramo = ramo
        militar.Atualizar()
    
    return redirect(url_for('militares'))

@app.route("/criar")
def criar():
    return render_template(
        "inserir.html"
    )

@app.route("/inserir",methods = ['POST'])
def inserir():
    if request.method == 'POST':
        nim =request.form ['nim']
        patente =request.form ['patente']
        cc =request.form ['cc']
        nome =request.form ['nome']
        apelido =request.form ['apelido']
        nif =request.form ['nif']
        ramo =request.form ['ramo']

        militar = Militar()
        militar.NIM = nim
        militar.Patente = patente
        militar.CC = cc
        militar.Nome = nome
        militar.Apelido = apelido
        militar.NIF = nif
        militar.Ramo = ramo
        militar.Inserir()
    
    return redirect(url_for('militares'))
@app.route('/webservice')
def webservice():
    if request.headers:
        print(request.headers)
        if request.headers["Token"]=="W74644#$":
            logging.error("valid token was provided")
            militares = Militar.ListaRegistos()
            lista = []
            for m in militares:
                lista.append(m.ToDictionary())
            strjson = Utils.ExportarJSON(lista)
            return jsonify(strjson)
        else:
            logging.warning("not authorized")
            return jsonify("not authorized")
    else:
        logging.error("No token was provided")
        return jsonify("not token was provided")

@app.route('/webservice/<id>')
def webservicedetail(id):
    m = Militar()
    m.Get(id)
    strjson = Utils.ExportarJSON(m.ToDictionary())
    return jsonify(strjson)

@app.route('/webservicepost',methods = ['POST'])
def webservicepost():
    if request.json:
        #hacking
        value = str(request.json).replace("'","\"")
        lista = Militar.ImportarDeJSON(Utils.ImpostarJSON(value))
        
        return jsonify(len(lista))
    else:
        return jsonify("error 400")
