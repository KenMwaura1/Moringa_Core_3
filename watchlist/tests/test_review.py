import unittest
from app.models import Review, User
from app import db


class ReviewCase(unittest.TestCase):
    """
    test class for the review model
    """

    # TODO: add tests for review
    def setUp(self):
        self.user_Zoo = User(username='Zoo', password='potato', email='zoo@zoo.com')
        self.new_review = Review(movie_id=12345, movie_title='test title',
                                 image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",
                                 movie_review='This movie is the best thing since sliced bread', user=self.user_Zoo)

    def tearDown(self):
        Review.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id, 12345)
        self.assertEquals(self.new_review.movie_title, 'test title')
        self.assertEquals(self.new_review.image_path, "https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.movie_review, 'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user, self.user_Zoo)

    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all()) > 0)

    def test_get_review_by_id(self):

        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)
