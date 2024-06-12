from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = '906ea9264ffdb333a17906a75bb048d6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hugo:hugo@localhost:5432/projet'

db = SQLAlchemy(app)

from . import routes