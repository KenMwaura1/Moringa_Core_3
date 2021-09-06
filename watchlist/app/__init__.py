from flask import Flask


# Initialize the application
app = Flask(__name__)

from . import views
