from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_options

bootstrap = Bootstrap()


def create_app(config_name):
    # Initialize the application
    app = Flask(__name__)

    # Creating the app configs
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting configuration
    from .request import configure_request
    configure_request(app)

    from .main import views
    from .main import error

    return app
