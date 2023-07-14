
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'q1w2e3r4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
api = Api(app)
db = SQLAlchemy(app)

from REST_APIs import routes
from REST_APIs import resources