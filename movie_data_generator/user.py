from .genre import Genre
from .profile import normalize
from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class User:
    coverage: float = field(repr=False)
    profile: dict[Genre, float] = field(repr=False)
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        self.coverage = round(self.coverage, 2)
        self.profile = normalize(self.profile)
