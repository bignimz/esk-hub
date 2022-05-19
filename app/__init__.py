import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import config_options
# from flask_mail import Mail




app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_name):
      app.config.from_object(config_options[config_name])
      db.init_app(app)
      login_manager.init_app(app)
      bcrypt.init_app(app)


      from app.auth.views import auth
      from app.posts.views import posts
      from app.main.views import main

      app.register_blueprint(auth)
      app.register_blueprint(posts)
      app.register_blueprint(main)


      return app