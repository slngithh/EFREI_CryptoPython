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
def exercice2(): 
    return render_template('exercice2.html')

@app.route('/exercice3')
def exercice3(): 
    return render_template('exercice3.html')

@app.route('/svg')
def svg(): 
    return render_template('svg.html')

@app.route('/maison')
def maison(): 
    return render_template('maison.html')

@app.route('/svg-cards')
def cards(): 
    return render_template('svg-cards.svg')

@app.route('/chenille')
def chen(): 
    return render_template('chenille.svg')

@app.route('/des')
def des():
  return render_template('jeu_de_des.html')

@app.route('/bibliotheque_images')
def des():
  return render_template('bibliotheque.html')
  
key = Fernet.generate_key()
f = Fernet(key)



if __name__ == "__main__":
  app.run(debug=True)
