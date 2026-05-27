import pymysql

def connetti():
    connessione = pymysql.connect( # crea un oggetto
        #host = "192.168.51.245",
        host= 'localhost',
        user = "frasimone07",
        password="Fraale_2021!",
        database = "frasimone07",
        cursorclass = pymysql.cursors.DictCursor
        # ritornami le tuple come dei dizionari

    )
    return connessione

connessione = connetti() # 1) connesione al DB
try:
    with connessione.cursor() as cursor:
        query = "select * from DOTTORI" # 2)ottengo il cursore
        cursor.execute(query) # eseguo interrogazione
        risultato = cursor.fetchall() # ottengo i risultati
        print(risultato)
finally:
    connessione.close()