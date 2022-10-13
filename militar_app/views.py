from flask import Flask,render_template
from militarcls import Militar
from . import app
@app.route("/")
def home():

    return render_template(
        "home.html"
        ,valor="Sergio Fontes"
    )

@app.route("/militares")
def militares():
    lista = Militar.ListaRegistos()
    return render_template(
        "militares.html"
        ,militares=lista
    )