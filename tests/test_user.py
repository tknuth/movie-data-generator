from movie_data_generator.user import User, intersecting_keys
from movie_data_generator.movie import Movie
from movie_data_generator.genre import Genre
from datetime import datetime


def test_intersecting_keys():
    assert intersecting_keys([{"a": 1, "b": 2}, {"a": 3, "c": 4}]) == {"a"}


def test_select_movie():
    a = Movie(
        title="A",
        year=2020,
        rating=1,
        popularity=1,
        profile={Genre.ACTION: 0.3, Genre.COMEDY: 0},
    )
    b = Movie(
        title="B",
        year=2020,
        rating=1,
        popularity=1,
        profile={Genre.ROMANCE: 0.3, Genre.DRAMA: 0.7},
    )
    user = User(
        age=18,
        signup_date=datetime(2024, 1, 1),
        watch_probability=1,
        profile={Genre.ACTION: 0.5, Genre.COMEDY: 0.5},
    )
    assert user.select_movie([a, b]) == a
