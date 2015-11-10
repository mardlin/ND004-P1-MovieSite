import webbrowser

class Movie():
    """This class stores movie specific information and enables you to play a movies trailer
    """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # set the instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)