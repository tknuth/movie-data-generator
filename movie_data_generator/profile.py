from .genre import *

Profile = dict[Genre, float]


def load_profiles():
    return (
        {Genre.ADVENTURE: 0.6, Genre.ACTION: 0.4},
        {Genre.THRILLER: 0.5, Genre.DRAMA: 0.5},  # crime, mystery
        {Genre.FANTASY: 0.5, Genre.ADVENTURE: 0.3, Genre.ANIMATION: 0.3},
        {Genre.DOCUMENTARY: 0.7, Genre.HISTORY: 0.3},  # realist
        {Genre.ROMANCE: 0.6, Genre.DRAMA: 0.2, Genre.COMEDY: 0.2},  # romcom/dramedy
        {Genre.WESTERN: 0.6, Genre.ACTION: 0.2, Genre.ADVENTURE: 0.2},
    )


def normalize(d: dict[Genre, float]):
    d = {**d}
    s = sum(d.values())
    for k, v in d.items():
        d[k] = v / s
    return d
