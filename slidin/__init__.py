from enum import unique
from logging import debug
from os import truncate
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ef89e27fedbcc1b6bc2deeeac4b97600'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) 

from slidin import routes