from flask import render_template, current_app
from . import app


# Views
@app.route('/')
def index():
    """
    root page view that returns the index page
    :return: index template
    """
    return render_template('index.html')


@app.route('/movie/<int:movie_id>')
def movie(movie_id: int):
    """
    movie view page that takes an id and returns movie details and data
    :param movie_id: integer reference to movie
    :return: movie details template
    """
    return render_template('movie.html', id=movie_id)

