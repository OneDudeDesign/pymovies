import media
import fresh_tomatoes

toystory = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A Marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")


apollo13 = media.Movie("Apollo 13",
                       "The greatest space rocket ever",
                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",
                       "https://youtu.be/nEl0NsYn1fU")

movies = [toystory,avatar,apollo13]

# fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__module__ + " is the module that the " + media.Movie.__name__ + " class exists in")




