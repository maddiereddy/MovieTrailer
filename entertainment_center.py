import media
import fresh_tomatoes

"""
This python file creates instances of the Movies class from the media file.
These movie objects are then stored in an array which is then passed as input
to the open_movies_page() function of the fresh_tomatoes file. This is used
build the HTML file which displays the Movie Trailer website
"""

#build the movie objects
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4", media.Movie.VALID_RATINGS[0], 1995)

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY", media.Movie.VALID_RATINGS[1], 2009)

school_of_rock = media.Movie("School of Rock",
                        "Using rock music to learn",
                        "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74", media.Movie.VALID_RATINGS[2], 2003)

ratatouille = media.Movie("Ratatouille",
                        "A rat is a chef in Paris",
                        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk", media.Movie.VALID_RATINGS[0], 2007)

midnight_in_paris = media.Movie("Midnight in Paris",
                        "Going back in time to meet authors",
                        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=atLg2wQQxvU", media.Movie.VALID_RATINGS[2], 2011)

hunger_games = media.Movie("Hunger Games",
                        "A really real reality show",
                        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=PbA63a7H0bo", media.Movie.VALID_RATINGS[2], 2012)


the_grand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
                            "A story about a concierge who is framed for murder",
                            "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
                            "https://www.youtube.com/watch?v=1Fg5iWmQjwk", media.Movie.VALID_RATINGS[0], 2014)

pulp_fiction = media.Movie("Pulp Fiction",
                "It is a 1994 American black comedy crime film written and directed by Quentin Tarantino",
                "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                "https://www.youtube.com/watch?v=s7EdQ4FqbhY", media.Movie.VALID_RATINGS[3], 1994)

the_usual_suspects = media.Movie("The Usual Suspects",
                "It is a 1995 American neo-noir crime thriller film",
                "https://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg",
                "https://www.youtube.com/watch?v=FIRKclHfbRs", media.Movie.VALID_RATINGS[3], 1995)

inception = media.Movie("Inception",
                "Inception is a 2010 science fiction heist thriller film",
                "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                "https://www.youtube.com/watch?v=8hP9D6kZseM", media.Movie.VALID_RATINGS[2], 2010)

the_matrix = media.Movie("The Matrix",
                "It depicts a dystopian future in which reality as perceived by most humans is actually a simulated reality",
                "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                "https://www.youtube.com/watch?v=vKQi3bBA1y8", media.Movie.VALID_RATINGS[3], 1999)

whiplash = media.Movie("Whiplash",
                "It depicts the relationship between an ambitious jazz student and an abusive instructor",
                "https://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg",
                "https://www.youtube.com/watch?v=tYkuvB2f5XU", media.Movie.VALID_RATINGS[3], 2014)


#create movies array containing the movie objects
movies = [inception, pulp_fiction, the_grand_budapest_hotel, the_matrix, the_usual_suspects, whiplash, avatar, hunger_games, midnight_in_paris, school_of_rock, toy_story, ratatouille]

#Pass the array as input to the open_movies_page() function which builds the
#html page to diplay the movie trailer website
fresh_tomatoes.open_movies_page(movies)

