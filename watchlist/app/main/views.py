from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user

from . import main
from ..request import get_movies, get_movie, search_movie
from ..models import Review, User
from ..main.forms import ReviewForm, UpdateProfile
from .. import db, photos


# Views
@main.route('/')
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
        return redirect(url_for('main.search', movie_name=search))
    title = "Home -  Welcome to the best Movie review website "
    return render_template('index.html', title=title, popular=popular_movies,
                           upcoming=upcoming_movies, now_showing=now_showing_movie)


@main.route('/movie/<int:movie_id>')
def movie(movie_id: int):
    """
    movie view page that takes an id and returns movie details and data
    :param movie_id: integer reference to movie
    :return: movie details template
    """
    movie = get_movie(movie_id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)
    return render_template('movie.html', title=title, movie=movie, reviews=reviews)


@main.route('/search/<string:movie_name>')
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
    return render_template('search.html', movies=searched_movies, title=title)


@main.route('/movie/review/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie_id=movie.id, movie_title=title, image_path=movie.poster, movie_review=review,
                            user=current_user)

        # save review method
        new_review.save_review()
        return redirect(url_for('.movie', id=movie.id))

    title = f'{movie.title} review'
    return render_template('new_review.html', title=title, review_form=form, movie=movie)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.update_profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))
