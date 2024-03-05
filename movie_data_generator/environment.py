from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .profile import Profile
    from .movie import Movie

from dataclasses import dataclass, field
from datetime import datetime

from .profile import load_profiles
from .movie import load_movies


@dataclass
class Environment:
    users: list[User] = field(default_factory=list)
    date: int = datetime(1990, 1, 1)
    profiles: list[Profile] = field(default_factory=load_profiles)
    movies: list[Movie] = field(default_factory=load_movies)

    @property
    def published_movies(self) -> list:
        return [m for m in self.movies if m.year <= self.date.year]