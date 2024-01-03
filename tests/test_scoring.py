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
    assert np.isclose(genre_match(a, b, k=2), 0.967, atol=0.001, rtol=0)
    assert np.isclose(genre_match(a, b, f, k=2), 0.982, atol=0.001, rtol=0)
