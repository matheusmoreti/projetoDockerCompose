#!/usr/bin/env python
import json
import traceback
import base64
import logging
from datetime import date, datetime
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'senhaFiap'
app.config['MYSQL_DATABASE_DB'] = 'projetoDC'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
mysql.init_app(app)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

@app.route("/")
def hello():
    return "Bem vindo! Essa API retorna lista de alunos. Para retornar a lista de alunos de Big Data, utilize getBigData; Para Marketing, getMarketing; Para Arquitetura de Solucoes, getArquitetura\n"


@app.route("/getBigData")
def getBigData():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from Alunos where CURSO = 'Big Data'")
        r = [dict((cursor.description[i][0], value)
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        json_string = json.dumps(r, default=json_serial)
        return json_string
    except Exception as e:
        return 'Erro /getDados' + str(e) + traceback.format_exc()

@app.route("/getMarketing")
def getMarketing():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from Alunos where CURSO = 'Marketing'")
        r = [dict((cursor.description[i][0], value)
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        json_string = json.dumps(r, default=json_serial)
        return json_string
    except Exception as e:
        return 'Erro /getDados' + str(e) + traceback.format_exc()    

@app.route("/getArquitetura")
def getArquitetura():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from Alunos where CURSO = 'Arquitetura de Solucoes'")
        r = [dict((cursor.description[i][0], value)
            for i, value in enumerate(row)) for row in cursor.fetchall()]
        json_string = json.dumps(r, default=json_serial)
        return json_string
    except Exception as e:
        return 'Erro /getDados' + str(e) + traceback.format_exc()        
    
if __name__ == "__main__":
    #teste()
    app.run(host='0.0.0.0',debug=True)
