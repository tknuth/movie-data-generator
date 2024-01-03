import functools as ft
import numpy as np
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


def profile_match(a: Profile, b: Profile, f: Optional[Callable] = None, k: float = 1):
    if f is None:
        f = sum_dim_shared_items(base=BASE)
    # for sum_dim_shared_items,
    # k=2 yields almost 1 with BASE=0.7
    # when at least two genres match perfectly
    return logistic_function(f(a, b), k)


def noise(mu: float = 0, std: float = 0.1):
    return np.random.normal(mu, std)


def score(
    user: User,
    movie: Movie,
    **kwargs: dict,
):
    # TODO: consider movie rating
    # TODO: consider user type
    # TODO: CI/CD, linting etc.
    p = profile_match(user.profile, movie.profile, **kwargs.get("profile_match", {}))
    e = noise(**kwargs.get("noise", {}))
    return p + e
