import unittest
from app.models import Movie


class MovieTestCase(unittest.TestCase):
    """
    Test class for the Movie class.
    """

    def setUp(self):
        """
        setUp method that will run before every test
        :return: new instance of Movie class
        """
        self.new_movie = Movie(1234, 'Python Must be crazy', 'A thrilling new Python series',
                                                             'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))


