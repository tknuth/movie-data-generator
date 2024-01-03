import random
import statistics
from dataclasses import dataclass

from movie_data_generator.movie import Movie
from movie_data_generator.user import User


# TODO: fix bug when popularity is zero, endless loop?
def sample_movies(user: User, l: list[Movie]):
    s = [movie for movie in l[:] if set(movie.profile) & set(user.profile)]
    w = [s.popularity for s in s]
    n = round(len(s) * user.coverage)
    c = set()
    while len(c) < n and len(set(s)) >= n:
        c.add(random.choices(s, w)[0])
    c = list(c)
    random.shuffle(c)
    return c


# assumes that additional genres are irrelevant
# and only differing values between genres matter
def similarity(a: dict, b: dict):
    if not (set(a) & set(b)):
        raise ValueError("No genres in common.")
    return statistics.mean(1 - abs(a[k] - b[k]) for k in set(a) & set(b))


@dataclass(frozen=True)
class Rating:
    movie: Movie
    user: User
    score: float


def create_rating(user: User, movie: Movie):
    return Rating(movie, user, similarity(user.profile, movie.profile))


def rate_movies(user: User, movies: list[Movie]):
    return [create_rating(user, movie) for movie in movies]


# def sample_and_rate_movies(user: User, movies: list[Movie]):
#     return rate_movies(user, sample_movies(user, movies))


def create_random_user(profiles):
    return User(coverage=random.uniform(0, 1), profile=random.choice(profiles))
