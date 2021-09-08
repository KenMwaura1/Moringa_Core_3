import json
import urllib.request

from .models import Movie

# Get the Api key for movie api
api_key = None

# get the movie base url
base_url = None

# get the movie base poster url
poster_url = None


def configure_request(app):
    global api_key, base_url, poster_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']
    poster_url = app.config['MOVIE_Poster_URL']


def get_movies_posters(poster_path):
    """

    :param poster_url:
    :return:
    """
    get_poster_url = poster_url.format(poster_path)
    url = urllib.request.urlopen(get_poster_url).read()
    poster = url
    print(get_poster_url)
    print(poster)


def get_movies(category: str):
    """
    Function that makes a request to TMDB Api and receives a JSON response.
    :param category: str
    :return: list of movies
    """
    get_movies_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)
        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_movie_results(movie_results_list)

    return movie_results


def get_movie(movie_id: int):
    """
    function to retrieve a single movie from the Api using the ID.
    :param movie_id: ID of the movie to get.
    :return: single movie object
    """

    get_movie_details_url = base_url.format(movie_id, api_key)

    def extract_movie(movie_details_response):
        id = movie_details_response.get('id')
        title = movie_details_response.get('original_title')
        overview = movie_details_response.get('overview')
        poster = movie_details_response.get('poster_path')
        vote_average = movie_details_response.get('vote_average')
        vote_count = movie_details_response.get('vote_count')
        return Movie(id, title, overview, poster, vote_average, vote_count)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)
        movie_object = None
        if movie_details_response:
            movie_object = extract_movie(movie_details_response)
    return movie_object


def process_movie_results(movie_list):
    """
    Function that processes movie list returned ny the API to a list of objects
    :param movie_list: list of dicts containing movie details
    :return: list of Movie Objects
    """
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster_path = movie_item.get('poster_path')

        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote-vote_count')

        if poster_path:
            movie_object = Movie(id, title, overview, poster_path, vote_average, vote_count)
            movie_results.append(movie_object)

    return movie_results


def search_movie(movie_name):
    search_movie_url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_name}'
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_movie_results(search_movie_list)
    return search_movie_results
