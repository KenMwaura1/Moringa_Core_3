from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Devconfig


# Initialize the application
app = Flask(__name__)

# Setup the Dev config
app.config.from_object(Devconfig)
app.config.from_pyfile('instance/config.py')

# Initialize Flask Extensions
bootstrap = Bootstrap(app)

from . import views
