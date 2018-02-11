import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-super-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/mydatabase.db'
db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
