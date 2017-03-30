import media

toystory = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life",
                       "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toystory.storyline)

avatar = media.Movie("Avatar",
                     "A Marine on an alien planet",
                     "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

print(avatar.storyline)

apollo13 = media.Movie("Apollo 13",
                       "The greatest space rocket ever",
                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Apollo_thirteen_movie.jpg",
                       "https://youtu.be/nEl0NsYn1fU")

print(apollo13.storyline)

apollo13.show_trailer()