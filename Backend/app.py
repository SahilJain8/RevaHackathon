from flask import Flask,render_template,request,jsonify,flash,redirect,url_for
import numpy as np
import os
from tensorflow import keras
import tensorflow as tf
from classfication import pred
from authlib.integrations.flask_client import OAuth
from monkeypox import predmonkey
from brain import predbrain

app=Flask(__name__,static_folder="assets")
oauth = OAuth(app)
 

app.secret_key = "secret key"
app.config['SERVER_NAME'] = 'localhost:5000'
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index.html')
def index():
    return render_template("index.html")


@app.route('/oct.html')
def oct():
    return render_template("oct.html")


@app.route('/contacts.html')
def contacts():
    return render_template("contacts.html")



@app.route('/login.html')
def login():
    return render_template("login.html")

    
@app.route('/contribute.html')
def contribute():
    return render_template("contribute.html")



    
@app.route('/api.html')
def api():
    return render_template("api.html")
@app.route('/monkeypox.html')
def monkey():
    return render_template('monkeypox.html')

@app.route('/Brain tumor.html')
def brain():
    return render_template('Brain tumor.html')

@app.route('/predection',methods = ['GET','POST'])
def predection():
    if request.method=="POST":
        file=request.files["image"]
        file.save(file.filename)
        img=tf.keras.utils.load_img(file.filename)
        state=pred(img)
        os.remove(file.filename)
        flash(str(state))

        return redirect('/contribute.html')
        

@app.route('/monkeypox',methods = ['GET','POST'])
def monkeypoxpred():
    if request.method=="POST":
        file=request.files["image"]
        file.save(file.filename)
        img=tf.keras.utils.load_img(file.filename)
        state=predmonkey(img)
        os.remove(file.filename)
        flash(str(state))

        return redirect('/contribute.html')

@app.route('/braintumor',methods = ['GET','POST'])
def brainpred():
    if request.method=="POST":
        file=request.files["image"]
        file.save(file.filename)
        img=tf.keras.utils.load_img(file.filename)
        state=predbrain(img)
        os.remove(file.filename)
        flash(str(state))

        return redirect('/contribute.html')





    
if __name__=="__main__":
    app.run(debug=True)




