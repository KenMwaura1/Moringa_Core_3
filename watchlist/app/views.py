from flask import render_template, current_app
from . import app
from .request import get_movies, get_movie


# Views
@app.route('/')
def index():
    """
    root page view that returns the index page and its data
    :return: index template
    """
    title = "Home -  Welcome to the best Movie review website "
    # Getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    return render_template('index.html', title=title, popular=popular_movies,
                           upcoming=upcoming_movies, now_showing=now_showing_movie)


@app.route('/movie/<int:movie_id>')
def movie(movie_id: int):
    """
    movie view page that takes an id and returns movie details and data
    :param movie_id: integer reference to movie
    :return: movie details template
    """
    movie = get_movie(movie_id)
    title = f'{movie.title}'
    print(movie)
    return render_template('movie.html', title=title, movie=movie)
