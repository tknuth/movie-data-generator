from dataclasses import dataclass, field

from toolz.curried import filter, map, pipe

from .genre import Genre


@dataclass(frozen=True)
class Movie:
    title: str
    year: int
    rating: float
    popularity: float
    profile: dict[Genre, float] = field(repr=False)

    def __hash__(self):
        return hash((self.title, self.year))

    @property
    def slug(self):
        title = pipe(
            self.title.lower(),
            filter(lambda c: c.isalnum() or c.isspace()),
            map(lambda c: c.replace(" ", "-")),
            lambda l: "".join(l),
        )
        return "-".join([title, str(self.year)])

    def to_dict(self):
        return {
            "slug": self.slug,
            "title": self.title,
            "year": self.year,
            "rating": self.rating,
            "popularity": self.popularity,
            "profile": {k.value: v for k, v in self.profile.items()},
        }

    def __repr__(self):
        return f"Movie(slug={self.slug})"


def load_movies():
    movies = (
        Movie(
            title="The Philosopher's Play",
            year=1998,
            popularity=0.6,
            rating=0.4,
            profile={
                Genre.FANTASY: 1.0,
                Genre.ADVENTURE: 0.5,
            },
        ),
        Movie(
            title="Echoes of the Past",
            year=2005,
            popularity=0.4,
            rating=0.9,
            profile={
                Genre.DRAMA: 0.5,
                Genre.ROMANCE: 0.5,
                Genre.FANTASY: 1.0,
            },
        ),
        Movie(
            title="The Great Cosmic Race",
            year=2020,
            rating=0.7,
            popularity=0.4,
            profile={
                Genre.ACTION: 1.0,
                Genre.ADVENTURE: 0.5,
                Genre.SCIFI: 1.0,
            },
        ),
        Movie(
            title="The Clockwork King",
            year=2022,
            popularity=0.6,
            rating=0.8,
            profile={
                Genre.THRILLER: 0.2,
                Genre.ADVENTURE: 0.1,
                Genre.FANTASY: 1.0,
            },
        ),
    )
    slugs = [m.slug for m in movies]
    # Assert no duplicates
    assert len(slugs) == len(set(slugs))
    return movies
