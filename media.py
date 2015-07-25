import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    #Class variable VALID_RATINGS is an array containing MPAA movie ratings
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    
    #Class constructor initializes the instance variables:
    #title, storyline, poster_image_url, trailer_youtube_url, rating and year
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_rating, movie_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
        self.year = movie_year

    #Class method show_trailer opens a web browser window and starts
    #the youtube movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
