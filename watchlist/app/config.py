import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    General configuration parent class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_POSTER_BASE_URL = 'https://image.tmdb.org/t/p/original{}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_SQLALCHEMY_DATABASE_URI")


class Devconfig(Config):
    """
    Development configuration child class
    :param: Config parent configuration class with general configuration settings.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True


class ProdConfig(Config):
    """
    Product configuration child class
    :param: Config: parent class with general configuration settings.
    """
    pass


config_options = {
    'development': Devconfig,
    'production': ProdConfig,
    'test': TestConfig
}
