from ensurepip import bootstrap
from decouple import config
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config('SECRET_KEY')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["MAIL_SERVER"] = config("MAIL_SERVER")
    app.config["MAIL_PORT"] = int(config("MAIL_PORT"))
    app.config["MAIL_USE_TLS"] = config("MAIL_USE_TLS")
    app.config["MAIL_USERNAME"] = config("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = config("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = config("MAIL_DEFAULT_SENDER")

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

    from app import routes
    routes.init_app(app)


    return app


