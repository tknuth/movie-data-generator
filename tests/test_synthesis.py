import random

from movie_data_generator.genre import *
from movie_data_generator.movie import *
from movie_data_generator.profile import *
from movie_data_generator.synthesis import *


def test_sample():
    users = [
        User(
            coverage=0.6,
            profile={Genre.FANTASY: 0.9, Genre.ANIMATION: 0.4},
        ),
        User(
            coverage=0.8,
            profile={Genre.FANTASY: 0.9, Genre.ANIMATION: 0.4},
        ),
    ]

    movies = [
        Movie(
            title="a",
            year=2010,
            popularity=0.9,
            rating=0.4,
            profile={Genre.FANTASY: 0.5, Genre.ADVENTURE: 0.5},
        ),
        Movie(
            title="b",
            year=2010,
            popularity=0.6,
            rating=0.4,
            profile={Genre.ACTION: 0.9, Genre.ADVENTURE: 0.5},
        ),
        Movie(
            title="c",
            year=2010,
            popularity=0.6,
            rating=0.4,
            profile={Genre.COMEDY: 0.5, Genre.ANIMATION: 0.8},
        ),
    ]

    random.seed(1)
    assert set(sample_movies(users[0], movies)) == set([movies[0]])
    assert set(sample_movies(users[1], movies)) == set([movies[0], movies[2]])


def test_create_random_user():
    random.seed(1)
    profiles = load_profiles()
    create_random_user(profiles)
