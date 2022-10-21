from datetime import datetime
from flask import Flask, render_template, url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URL'] = sqlite:///site.db
db = SQLAlchemy(app)

@app.route("/")
@app.rote("/home")
def home():
    return render_template('home.html')