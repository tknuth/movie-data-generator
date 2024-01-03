import functools as ft
import math
from typing import Callable, Iterable, Optional

import toolz.curried as tz

from .movie import Movie
from .profile import Profile
from .user import User

BASE = 0.7


def intersecting_keys(l: list[dict]) -> set[str]:
    return ft.reduce(set.intersection, map(set, l))


def filter_shared_items(l: list[dict]) -> Iterable[dict]:
    return map(tz.keyfilter(lambda k: k in intersecting_keys(l)), l)


def min_of_shared_items(l: list[dict]) -> list[float]:
    return list(tz.merge_with(min, filter_shared_items(l)).values())


def sum_dim_values(l: list[float], base: float) -> float:
    return sum([v * base**i for i, v in enumerate(l)])


@tz.curry
def logistic_function(x: float, k: float = 1) -> float:
    return 1 / (1 + math.exp(k * -x))


@tz.curry
def sum_dim_shared_items(a: Profile, b: Profile, base: float):
    return sum_dim_values(min_of_shared_items([a, b]), base)


def genre_match(a: Profile, b: Profile, f: Optional[Callable] = None, k: float = 1):
    if f is None:
        f = sum_dim_shared_items(base=BASE)
    # for sum_dim_shared_items,
    # k=2 yields almost 1 with BASE=0.7
    # when at least two genres match perfectly
    return logistic_function(f(a, b), k)


def score(user: User, movie: Movie, genre_match_kwargs: dict = None):
    # TODO: add noise
    # TODO: consider movie rating
    # TODO: consider user type
    # TODO: CI/CD, linting etc.
    if genre_match_kwargs is None:
        genre_match_kwargs == {}
    return genre_match(user.profile, movie.profile, **genre_match_kwargs)
