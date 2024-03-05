import functools as ft
import random
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import uuid4

import numpy as np
from loguru import logger

from .environment import Environment
from .rating import Rating
from .genre import Genre
from .movie import Movie
from .profile import normalize


@dataclass
class User:
    age: int
    signup_date: datetime
    watch_probability: float = field(repr=False)
    profile: dict[Genre, float] = field(repr=False)
    history: dict[str, Rating] = field(default_factory=dict)
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        self.watch_probability = round(self.watch_probability, 2)
        self.profile = normalize(self.profile)

    def make_turn(self, env: Environment):
        if random.random() < self.watch_probability:
            self.watch_movie(env)

    def watch_movie(self, env: Environment):
        movie = self.select_movie(env.published_movies)
        if not movie:
            return
        rating = self.rate_movie(movie)
        self.history[movie.slug] = rating
        logger.info(f"{env.date}: User rated '{movie.title}' with {rating.score}.")

    def has_watched_before(self, movie: Movie) -> bool:
        return movie.slug in self.history

    def shared_genres(self, movie: Movie) -> set[Genre]:
        return intersecting_keys([self.profile, movie.profile])

    def select_movie(self, movies: list[Movie]) -> Optional[Movie]:
        candidates = []
        for movie in movies:
            if not self.has_watched_before(movie) and self.shared_genres(movie):
                candidates.append(movie)
        if candidates:
            return random.choice(candidates)

    def rate_movie(self, movie: Movie) -> Rating:
        score = round(clamp(movie.rating + noise()), 2)
        return Rating(user=self, movie=movie, score=score)


def intersecting_keys(l: list[dict]) -> set[str]:
    return ft.reduce(set.intersection, map(set, l))


def noise(mu: float = 0, std: float = 0.1):
    return np.random.normal(mu, std)


def clamp(x, lower=0, upper=1):
    return max(lower, min(x, upper))
