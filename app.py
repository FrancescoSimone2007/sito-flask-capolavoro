from flask import Flask, render_template
#from dati import *
from provadb import *
import pymysql

app = Flask(__name__)
'''
def connetti():
    connessione = pymysql.connect( # crea un oggetto
        # host = "192.168.51.245",
        host= 'localhost',
        user = "frasimone07",
        password="Fraale_2021!",
        database = "frasimone07",
        cursorclass = pymysql.cursors.DictCursor
        # ritornami le tuple come dei dizionari

    )
    return connessione
'''
@app.route("/")
def home():
    connessione = connetti() # 1) connesione al DB
    try:
        with connessione.cursor() as cursor:
            query = "select * from DOTTORI" # 2)ottengo il cursore
            cursor.execute(query) # eseguo interrogazione
            risultato = cursor.fetchall() # ottengo i risultati
            print(risultato)
    finally:
        connessione.close()
    #return render_template("dottori.html", dottori=risultato)
    return render_template("home.html")

@app.route("/dottori")
def dottori():
    connessione = connetti() # 1) connesione al DB
    try:
        with connessione.cursor() as cursor:
            query = "select * from DOTTORI" # 2)ottengo il cursore
            cursor.execute(query) # eseguo interrogazione
            risultato = cursor.fetchall() # ottengo i risultati
            print(risultato)
    finally:
        connessione.close()
    return render_template("dottori.html",dottori=risultato)


@app.route("/pazienti")
def pazienti():
    connessione = connetti() # 1) connesione al DB
    try:
        with connessione.cursor() as cursor:
            query = "select * from PAZIENTI" # 2)ottengo il cursore
            cursor.execute(query) # eseguo interrogazione
            risultato = cursor.fetchall() # ottengo i risultati
            print(risultato)
    finally:
        connessione.close()
    return render_template("pazienti.html", paziente=risultato)

@app.route("/visite/<codice>/<tipo>")
@app.route("/visite")
def visite(codice=None, tipo=None):

    lista_filtrata = []
    connessione = connetti() # 1) connesione al DB
    try:
        with connessione.cursor() as cursor:
            query = "select * from APPUNTAMENTI" # 2)ottengo il cursore
            cursor.execute(query) # eseguo interrogazione
            risultato = cursor.fetchall() # ottengo i risultati
            print(risultato)
    finally:
        connessione.close()

    if tipo == "Dottore":
        for i in risultato:
            if i["CODDOTTORE"] == codice:
                lista_filtrata.append(i)

    elif tipo == "Paziente":
        for i in risultato:
            if codice == i["CF"]:
                lista_filtrata.append(i)

    else:
        lista_filtrata = risultato
    print(f"Lista filtrta:{lista_filtrata}")
    return render_template("visite.html",
                           lista_filtrata=lista_filtrata,
                           codice=codice,
                           tipo=tipo)
                           


if __name__ == "__main__":
    app.run(debug=True)