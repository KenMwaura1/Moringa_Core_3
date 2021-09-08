class Config:
    """
    General configuration parent class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_POSTER_BASE_URL = 'https://image.tmdb.org/t/p/original{}'


class Devconfig(Config):
    """
    Development configuration child class
    :param: Config parent configuration class with general configuration settings.
    """
    DEBUG = True


class ProdConfig(Config):
    """
    Product configuration child class
    :param: Config: parent class with general configuration settings.
    """
    pass
