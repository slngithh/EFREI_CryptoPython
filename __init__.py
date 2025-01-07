from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3 
                                                                                                                                       
app = Flask(__name__)                                                                                                                 
                                                                                                                                       
@app.route('/exercice1')
def exercice1(): 
    return render_template('exercice1.html')

@app.route('/exercice2')
def hello_world(): 
    return render_template('exercice2.html')

@app.route('/exercice3')
def hello_world(): 
    return render_template('exercice3.html')

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:token_encrypted>')
def decryptage(token_encrypted):
    valeur_decryptee = f.decrypt(token_bytes).decode()  # Décoder en str
    token_bytes = token_encrypted.encode()
    return f"Valeur décryptée : {valeur_decryptee}"


if __name__ == "__main__":
  app.run(debug=True)
