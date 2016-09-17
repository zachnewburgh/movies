import media
import fresh_tomatoes

# Instances of the Movie class.
gladiator = media.Movie("Gladiator",
                        "A disgraced general becomes a gladiator and reclaims Rome from an illegitimate emperor",
                        "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
                        "https://www.youtube.com/watch?v=owK1qxDselE")

the_notebook = media.Movie("The Notebook",
                        "A classic love story with a unique twist.",
                        "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
                        "https://www.youtube.com/watch?v=FC6biTjEyZw")

good_will_hunting = media.Movie("Good Will Hunting",
                     "A university janitor is discovered to be a genius who turns his life around with the help of a university professor",
                     "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",
                     "https://www.youtube.com/watch?v=nH9LZOXBMUE")

hook = media.Movie("Hook",
                     "A man who rediscovers his will to 'never grow up'.",
                     "https://upload.wikimedia.org/wikipedia/en/0/0e/Hook_poster_transparent.png",
                     "https://www.youtube.com/watch?v=LxnR9e7M8Vw")

dead_poets_society = media.Movie("Dead Poets Society",
                     "A new boarding school teacher inspires his students through unorthodox pedagogy",
                     "https://upload.wikimedia.org/wikipedia/en/4/49/Dead_poets_society.jpg",
                     "https://www.youtube.com/watch?v=4lj185DaZ_o")

selma = media.Movie("Selma",
                     "A retelling of the historic Selma to Montgomery March",
                     "https://upload.wikimedia.org/wikipedia/en/8/8f/Selma_poster.jpg",
                     "https://www.youtube.com/watch?v=x6t7vVTxaic")

# List of movies.
movies = [gladiator, the_notebook, good_will_hunting, hook, dead_poets_society, selma]

# Opens and formats the list of movies in the web browser.
fresh_tomatoes.open_movies_page(movies)
