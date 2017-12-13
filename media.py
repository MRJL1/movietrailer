import webbrowser
class Movie():
    """ This class is made to store detailed information regarding movies."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """initialises Movie class variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens Movie trailer in the web browser"""
        webbrowser.open(self.trailer_youtube_url)
