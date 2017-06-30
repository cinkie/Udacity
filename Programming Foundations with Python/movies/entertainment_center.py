
import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his torys that come to life.",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


##print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://s-media-cache-ak0.pinimg.com/originals/f7/bc/7b/f7bc7b19e7f8555ba0f36aa3f2bc5dcd.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

##print(avatar.storyline)

# avatar.show_trailer()

lalaland = media.Movie("La La Land",
	"Two proper L.A. dreamers, a suavely charming soft-spoken jazz pianist and a brilliant vivacious playwright, while waiting for their big break, attempt to reconcile aspirations and relationship in a magical old-school romance.",
	"https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_SY1000_SX675_AL_.jpg",
	"https://www.youtube.com/watch?v=DBUXcNTjviI")

attack_on_titan = media.Movie("Attack on Titan Season 2",
	"Human attacked by Titans",
	"https://vignette4.wikia.nocookie.net/shingekinokyojin/images/a/a5/Attack_on_Titan_Season_2_Official_Poster.png/revision/latest?cb=20160703181433",
	"https://www.youtube.com/watch?v=vmWAEQ8qIc4")

movies = [toy_story, avatar, lalaland, attack_on_titan]
# fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
