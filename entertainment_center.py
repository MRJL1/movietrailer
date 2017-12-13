import media
import fresh_tomatoes

#ironman movie: movie title, storyline, poster image and movie trailer
iron_man = media.Movie(
    "Iron Man",
    "a billionaire is a superhero",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
    "https://www.youtube.com/watch?v=LWbjrFCecPY")
#batman begins movie: movie title, storyline, poster image and movie trailer
batman_begins = media.Movie(
    "Batman Begins",
    "a billionaire is a superhero",
    "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
    "https://www.youtube.com/watch?v=neY2xVmOfUM")
#wonder woman movie: movie title, storyline, poster image and movie trailer
wonder_woman = media.Movie(
    "Wonder Woman",
    "A woman discovers that she is a goddess",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg", # NOQA
    "https://www.youtube.com/watch?v=VSB4wGIdDwo")
#thor movie: movie title, storyline, poster image and movie trailer
thor = media.Movie(
    "Thor",
    "A god kills his brother",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
    "https://www.youtube.com/watch?v=JOddp-nlNvQ")
#set the movies that will be passe to the media file
movies = [iron_man, batman_begins, wonder_woman, thor]
#open the HTML file in a webbrowser vis the fresh_totmates.py file
fresh_tomatoes.open_movies_page(movies)
