import media
import fresh_tomatoes

iron_man = media.Movie("Iron Man",
                     "a billionaire playboy philanthopist becomes a superhero by designing his own power suit",
                     "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                      "https://www.youtube.com/watch?v=LWbjrFCecPY",
                      "2008")

batman_begins = media.Movie("Batman Begins",
                     "a billionaire becomes a superhero by dressing up as bat",
                     "https://upload.wikimedia.org/wikipedia/en/a/af/Batman_Begins_Poster.jpg",
                      "https://www.youtube.com/watch?v=neY2xVmOfUM",
                      "2005")

wonder_woman = media.Movie("Wonder Woman",
                     "A goddesss discovers that she is a goddess",
                     "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                      "https://www.youtube.com/watch?v=VSB4wGIdDwo",
                      "2017")

thor = media.Movie("Thor",
                     "A god lands on earth and kills his adapted brother",
                     "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                      "https://www.youtube.com/watch?v=JOddp-nlNvQ",
                      "2010")

movies = [iron_man, batman_begins, wonder_woman, thor]
fresh_tomatoes.open_movies_page(movies)
 
