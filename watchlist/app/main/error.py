from flask import render_template
from . import main


@main.app_errorhandler(404)
def error_handler(error):
    """
    function to render 404 error message.
    :param error:
    :return: 404 error page
    """
    return render_template('watchlist/app/templates/404.html'), 404
