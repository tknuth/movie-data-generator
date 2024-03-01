from .genre import *
import copy

Profile = dict[Genre, float]


def load_profiles():
    return copy.copy(
        [
            {Genre.ADVENTURE: 6, Genre.ACTION: 4},
            {Genre.THRILLER: 5, Genre.DRAMA: 5},  # crime, mystery
            {Genre.FANTASY: 5, Genre.ADVENTURE: 3, Genre.ANIMATION: 3},
            {Genre.DOCUMENTARY: 7, Genre.HISTORY: 3},  # realist
            {Genre.ROMANCE: 6, Genre.DRAMA: 2, Genre.COMEDY: 2},  # romcom/dramedy
            {Genre.WESTERN: 6, Genre.ACTION: 2, Genre.ADVENTURE: 2},
        ]
    )


def normalize(d: dict[Genre, float]):
    d = {**d}
    s = sum(d.values())
    for k, v in d.items():
        d[k] = v / s
    return d
