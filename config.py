import os
import re




class Config:
      SQLALCHEMY_TRACK_MODIFICATIONS = False
      SECRET_KEY = os.environ.get('SECRET_KEY')
      MAIL_SERVER = 'smtp.gmail.com'
      MAIL_PORT = 587
      MAIL_USE_TLS = True
      MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
      MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
      SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    #   if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #         SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://",1)

class DevConfig(Config):
      SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nimrod:*admin*@localhost:5432/one_mic'
      DEBUG = True


config_options = {
      'development': DevConfig,
      'production': ProdConfig,
}