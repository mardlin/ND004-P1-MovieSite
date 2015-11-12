import media #imports the file media.py and classes within it
import fresh_tomatoes #import fresh_tomatoes.py

# Create an obeject instance of the class Movie, from the media module to hold 
# information about a movie
quest_for_fire = media.Movie("Quest for Fire",
         "A Science Fantasy Adventure",
         "https://upload.wikimedia.org/wikipedia/en/1/1f/Quest_for_Fire_%28movie_poster%29.jpg",
         "https://www.youtube.com/watch?v=2pcGGKtPpSE",
         "The film begins with a raid by the apelike Wagabu tribe on the early Homo sapiens Ulam tribe, who possess fire in the form of a carefully guarded small flame which they use to start larger bonfires. Obtained from a natural source, the flame is kept in a fabricated bone satchel and must be fed constantly to keep it alive, because the Ulam don't know how to start a fire. Driven out of their home after a bloody battle with the Wagabu, the surviving Ulam escape but are chased into a marsh by a pack of wolves. The Ulam's bald-headed fire tender escapes with the tribe's remaining fire; however, while crossing a marsh, he all but douses the embers, leaving the tribe doomed to die from exposure and starvation. The Ulam elder decides to send three men,...",
         "https://en.wikipedia.org/wiki/Quest_for_Fire_(film)"
         ) 


training_day = media.Movie("Training Day",
        "The only thing more dangerous than the line being crossed, is the cop who will cross it.",
        "https://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",
        "https://www.youtube.com/watch?v=gKTVQPOH8ZA",
        "The film follows a day in the life of Los Angeles Police Department officer, Jake Hoyt, who is scheduled to be evaluated by Detective Alonzo Harris, a highly decorated LAPD narcotics officer. In Alonzo's car, the officer sees teenage Mara Salvatrucha gang members dealing drugs in a park. Alonzo confiscates the drugs and tells Jake to take a hit of the marijuana. Jake refuses, but Alonzo puts a gun to his head and...",
        'https://en.wikipedia.org/wiki/Training_Day'
        )

            
the_royal_tenenbaums = media.Movie("The Royal Tenenbaums", 
        "Family Isn't A Word... It's A Sentence.",
        "https://upload.wikimedia.org/wikipedia/en/3/3b/The_Tenenbaums.jpg",
        "www.youtube.com/watch?v=8Eg6yIwP2vs",
        "Royal Tenenbaum explains to his three children, Chas, Margot, and Richie, that he and his wife, Etheline, are separating. Each of the Tenenbaum children achieved great success at a very young age. Chas is a math and business genius, from whom Royal steals money. Margot, who was adopted by the Tenenbaums, was awarded a grant for a play that she wrote in the ninth grade. Richie is a tennis prodigy and artist. He expresses his love for adopted sister Margot through many paintings. Royal takes him on regular outings, to which neither of the other children are invited. Eli Cash is the Tenenbaums' neighbor, and Richie's best friend.",
        "https://en.wikipedia.org/wiki/The_Royal_Tenenbaums"
        )
#place our Movie instance objects into a list
movies = [quest_for_fire, training_day, the_royal_tenenbaums]

#generates the fresh tomatoes site for the given movies
fresh_tomatoes.open_movies_page(movies)