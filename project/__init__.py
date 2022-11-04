from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_ckeditor import CKEditor



def create_app():
    app = Flask(__name__,template_folder="template")
    app.config['SECRET_KEY'] ="THIS IS A KEY LOL"

    ckeditor = CKEditor(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")

    return app