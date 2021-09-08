from flask import render_template, request, redirect, url_for
from watchlist.app import app
from watchlist.app.models.reviews import Review
from watchlist.app.request import get_movies, get_movie, search_movie
from watchlist.app.models import reviews
from watchlist.app.main.forms import ReviewForm

Review = reviews.Review


# Views
@app.route('/')
def index():
    """
    root page view that returns the index page and its data
    :return: index template
    """
    # Getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')

    search = request.args.get('movie_query')
    if search:
        return redirect(url_for('search_movie', movie_name=search))
    title = "Home -  Welcome to the best Movie review website "
    return render_template('watchlist/app/templates/index.html', title=title, popular=popular_movies,
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
    reviews = Review.get_reviews(movie.id)
    return render_template('watchlist/app/templates/movie.html', title=title, movie=movie, reviews=reviews)


@app.route('/search/<string:movie_name>')
def search(movie_name: str):
    """
    view function to display search results
    :param movie_name: name of movie to search for
    :return: results of search
    """
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('watchlist/app/templates/search.html', movies=searched_movies, title=title)


@app.route('/movie/review/new/<int:id>', methods=['GET', 'POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id, title, movie.poster, review)
        new_review.save_review()
        return redirect(url_for('movie', movie_id=movie.id))

    title = f'{movie.title} review'
    return render_template('watchlist/app/templates/new_review.html', title=title, review_form=form, movie=movie)
