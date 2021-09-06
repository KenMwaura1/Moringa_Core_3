class Movie:
    """
    class to define Movie objects
    """

    def __init__(self, id: int, title: str, overview: str,
                 poster: str, vote_average: int, vote_count: int):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = poster
        self.vote_average = vote_average
        self.vote_count = vote_count
