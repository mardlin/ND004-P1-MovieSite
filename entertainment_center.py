import media #this line imports the file media.py
import fresh_tomatoes

# Create an obeject instance of the class Movie, from the media module to hold 
# information about a movie
quest_for_fire = media.Movie("Quest for Fire",
         "A Science Fantasy Adventure",
         "https://upload.wikimedia.org/wikipedia/en/1/1f/Quest_for_Fire_%28movie_poster%29.jpg",
         "https://www.youtube.com/watch?v=2pcGGKtPpSE"
         ) 

training_day = media.Movie("Training Day",
        "The only thing more dangerous than the line being crossed, is the cop who will cross it.",
        "https://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",
        "https://www.youtube.com/watch?v=gKTVQPOH8ZA"
        )
            
the_royal_tenenbaums = media.Movie("The Royal Tenenbaums", 
        "Family Isn't A Word... It's A Sentence.",
        "https://upload.wikimedia.org/wikipedia/en/3/3b/The_Tenenbaums.jpg",
        "www.youtube.com/watch?v=8Eg6yIwP2vs"
        )

movies = [quest_for_fire, training_day, the_royal_tenenbaums]
#fresh_tomatoes.open_movies_page(movies)

print(quest_for_fire)