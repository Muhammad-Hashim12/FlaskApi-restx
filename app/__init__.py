from flask import Flask
from .extentions import *
from .routes import *
from .models import *


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:hashi@localhost/Enrolment'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY']="thisissecret"
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    api.add_namespace(ns)
    
    return app
