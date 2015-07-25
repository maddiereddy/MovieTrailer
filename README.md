# MovieTrailer
Udacity Project1
Introduction

Fresh Tomatoes is a Movie Trailer website where users can see my favorite movies and watch the trailers. 

Installation

User will have to unzip the uploaded zip file.
It will consist of a folder with three python files:

entertainment_center.py
media.py
fresh_tomatoes.py

It also contains the compiled fresh_tomotoes and media python files.
Also included is the fresh_tomatoes.html file

Running the website

You will need to have Python 2 installed on your computer. This includes the Idle editor for viewing and running the python files.

Open the file entertainment.py in IDLE and run it. It will open your web browser and display the 12 movies. Clicking on the movie poster starts the movie trailer in a popup modal window. Hovering the cursor over the movie title diplays a brief storyline of movie as a tooltip.


Since the zip folder also includes the fresh_tomatoes.html file, you could also just run that file in your web browser.

Description of included files

media.py contains the class Movie, a class variable of an array of MPAA movie ratings, a class constructor for initializing all the instance variables and a class method show_trailer() which opens a web browser to run the movie trailer.

entertainment.py contains the 12 movie objects created and placed in an array called movies. This array is in turn passed as input to the open_moves_page() function of the included fresh_tomatoes.py file.
The file media.py is also included.

fresh_tomatoes.py, which was provided, was altered to include three more variables: movie_storyline, movie_year and movie_rating.

movie_storyline is displayed as a tooltip when the cursor is hovered over the movie title.
movie_year and movie_rating are added below the movie title.
Clicking on the movie poster will start up the movie trailer in a modal window.

