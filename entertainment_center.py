import fresh_tomatoes
import media

# Create some Movie instances
logan = media.Movie("Logan", "The last wolverine movie",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
    "https://www.youtube.com/watch?v=RH3OxVFvTeg")

iron_man = media.Movie("Iron Man", "Iron Man origin story",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
    "https://www.youtube.com/watch?v=8hYlB38asDY")

iron_man_2 = media.Movie("Iron Man 2", "Sequel to Iron Man",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
    "https://www.youtube.com/watch?v=BoohRoVA9WQ")

dr_strange = media.Movie("Dr. Strange", "Sequel to Iron Man",
    "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
    "https://www.youtube.com/watch?v=HSzx-zryEgM")

#This is the list we supply to fresh_tomatoes
movies = [logan, iron_man, iron_man_2, dr_strange]

# Create the page using the data in movies
fresh_tomatoes.open_movies_page(movies)