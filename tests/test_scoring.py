import random

import numpy as np

from movie_data_generator.genre import Genre
from movie_data_generator.scoring import *


def test_intersecting_keys():
    a = {Genre.WESTERN: 0.8, Genre.SCIFI: 0.8, Genre.ADVENTURE: 0.3}
    b = {Genre.WESTERN: 0.4, Genre.DRAMA: 0.5, Genre.ADVENTURE: 0.7}
    c = {Genre.WESTERN: 0.4, Genre.DRAMA: 0.5, Genre.ADVENTURE: 0.2}
    assert intersecting_keys([a, b, c]) == {Genre.WESTERN, Genre.ADVENTURE}


def test_filter_shared_items():
    a = {Genre.WESTERN: 0.8, Genre.SCIFI: 0.8, Genre.ADVENTURE: 0.3}
    b = {Genre.WESTERN: 0.4, Genre.DRAMA: 0.5, Genre.ADVENTURE: 0.7}
    p = {Genre.WESTERN: 0.8, Genre.ADVENTURE: 0.3}
    q = {Genre.WESTERN: 0.4, Genre.ADVENTURE: 0.7}
    assert list(filter_shared_items([a, b])) == [p, q]


def test_min_of_shared_items():
    a = {Genre.WESTERN: 0.8, Genre.SCIFI: 0.8, Genre.ADVENTURE: 0.3}
    b = {Genre.WESTERN: 0.4, Genre.DRAMA: 0.5, Genre.ADVENTURE: 0.7}
    assert min_of_shared_items([a, b]) == [0.4, 0.3]


def test_sum_dim_values():
    assert sum_dim_values([0.4, 0.3], 0.5) == 0.4 * 0.5**0 + 0.3 * 0.5**1


def test_sum_dim_shared_items():
    a = {Genre.WESTERN: 1.0, Genre.SCIFI: 0.8, Genre.ADVENTURE: 1.0}
    b = {Genre.WESTERN: 1.0, Genre.DRAMA: 0.5, Genre.ADVENTURE: 1.0}
    assert sum_dim_shared_items(base=1)(a, b) == 2


def test_score_genre_fit():
    a = {Genre.WESTERN: 1.0, Genre.SCIFI: 0.8, Genre.ADVENTURE: 1.0}
    b = {Genre.WESTERN: 1.0, Genre.DRAMA: 0.5, Genre.ADVENTURE: 1.0}
    f = sum_dim_shared_items(base=1)
    assert np.isclose(profile_match(a, b, k=2), 0.967, atol=0.001, rtol=0)
    assert np.isclose(profile_match(a, b, f, k=2), 0.982, atol=0.001, rtol=0)


def test_clamp():
    assert clamp(+0.5) == 0.5
    assert clamp(+1.3) == 1.0
    assert clamp(-0.9) == 0.0


def test_score():
    user = User(
        coverage=0.6,
        profile={
            Genre.FANTASY: 0.9,
            Genre.ANIMATION: 0.4,
        },
    )

    movie = Movie(
        title="a",
        year=2010,
        popularity=0.9,
        rating=0.4,
        profile={
            Genre.FANTASY: 0.5,
            Genre.ADVENTURE: 0.5,
        },
    )

    a = score(user, movie)
    b = score(user, movie)
    c = score(user, movie)

    assert 0 < a < 1
    assert 0 < b < 1
    assert 0 < c < 1

    assert not np.isclose(a, b, atol=0.001, rtol=0)
    assert not np.isclose(b, c, atol=0.001, rtol=0)
