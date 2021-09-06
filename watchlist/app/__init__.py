from flask import Flask
from .config import Devconfig


# Initialize the application
app = Flask(__name__)

# Setup the Dev config
app.config.from_object(Devconfig)

from . import views
