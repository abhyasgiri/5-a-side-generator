from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////tmp/football_db' 
app.config["SECRET_KEY"] = "secret"
db = SQLAlchemy(app)

from application.models import Players

db.create_all()


from application import routes