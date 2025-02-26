from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow requests from React

    # Database Configuration (Choose SQLite or MySQL)
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/reactpython"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Email Configuration (Set Here)
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = "kirubaasagar88@gmail.com"
    app.config["MAIL_PASSWORD"] = "ufds lqcp qvyo bnke"  # Move to environment variable in production

    db.init_app(app)
    mail.init_app(app)

    # Import routes
    from app.routes import main
    app.register_blueprint(main)

    return app
