from enum import Enum


class Genre(Enum):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    ANIMATION = "Animation"
    COMEDY = "Comedy"
    DOCUMENTARY = "Documentary"
    DRAMA = "Drama"
    FANTASY = "Fantasy"
    HISTORY = "History"
    ROMANCE = "Romance"
    SCIFI = "Science Fiction"
    THRILLER = "Thriller"
    WESTERN = "Western"

    def __repr__(self):
        return self.name
