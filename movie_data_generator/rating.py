from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .movie import Movie
    from .user import User


@dataclass(frozen=True)
class Rating:
    movie: Movie
    user: User
    score: float
