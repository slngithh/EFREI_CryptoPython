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

key = Fernet.generate_key()
f = Fernet(key)



if __name__ == "__main__":
  app.run(debug=True)
