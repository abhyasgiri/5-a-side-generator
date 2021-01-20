from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv 

db = SQLAlchemy(app)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "DATABASE_URI"
db = SQLAlchemy(app)

from application.models import Players

db.create_all()


from application import routes