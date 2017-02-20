import media
import fresh_tomatoes

# creating object for each movie

good_will_hunting = media.Movie("Good Will Hunting",
                                "Will Hunting, a janitor at M.I.T., has a gift"
                                " for mathematics, but needs help from "
                                "a psychologist to find direction in his life.",
                                "https://s-media-cache-ak0.pinimg.com/736x/5a/87/81/5a8781b6b7b2a2fcc0653af9e739c394.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")

the_salesman = media.Movie("The Salesman",
                           "Forushande (The Salesman) is the story of a couple"
                           " whose relationship begins to turn sour during "
                           "their performance of Arthur Miller's "
                           "Death of a Salesman.",
                           "http://awardswatch.com/wp-content/uploads/2016/11/salesman-poster-new.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=r-61yYjKHHc")

sherolck_holmes = media.Movie("Sherlock Holmes",
                           "Detective Sherlock Holmes and his stalwart partner"
                           " Watson engage in a battle of wits and brawn with "
                           "a nemesis whose plot is a threat to all of England",
                           "http://image.tmdb.org/t/p/w342/Ah4nKoiUxRPdBnoJ3r5tw2UrGqp.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=J7nJksXDBWc")


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "http://img.csfd.cz/files/images/user/profile/159/129/159129345_9e5fe4.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock",
                             "After being kicked out of a rock band, Dewey Finn"
                             " becomes a substitute teacher of a strict "
                             "elementary private school, only to try and "
                             "turn it into a rock band.",
                             "http://www.hd-compare.de/_cover/school_of_rock_dvd.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")


ratatouille = media.Movie("Ratatouille",
                          "A rat who can cook makes an unusual alliance with "
                          "a young kitchen worker at a famous restaurant.",
                          "http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "While on a trip to Paris with his fiancée's "
                                "family, a nostalgic screenwriter finds himself"
                                " mysteriously going back to the 1920s "
                                "everyday at midnight.",
                                "https://natashastander.files.wordpress.com/2014/07/mip.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Game",
                           "Katniss Everdeen voluntarily takes her younger "
                           "sister's place in the Hunger Games, a televised "
                           "competition in which two teenagers from each of "
                           "the twelve Districts of Panem are chosen at random"
                           " to fight to the death.",
                           "http://im.rediff.com/movies/2013/dec/30hollywood-films7.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

# list contains all movie objects
movies = [good_will_hunting, the_salesman, sherolck_holmes, toy_story, avatar,
          school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# call open_movies_page to create a static website for movies list
fresh_tomatoes.open_movies_page(movies)
