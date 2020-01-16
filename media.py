import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer, watch_movie):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer
        self.movie_url = watch_movie



    def show_trailer(self):
        webbrowser.open(self.triler_youtube_url)
    def show_movie(self):
        webbrowser.open(self.movie_url)
