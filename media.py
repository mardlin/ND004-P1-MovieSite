import webbrowser

class Movie():
    """This class stores movie specific information and enables you to play a movie's trailer
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, details, wiki_url):
        # set the instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.details = details
        self.wiki_url = wiki_url
        self.slug = movie_title.replace(" ","-").lower()
        
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        print("go there your damn self " + self.trailer_youtube_url)