from movie_data_generator.profile import normalize
from movie_data_generator.genre import Genre


def test_normalize():
    a = {Genre.WESTERN: 0.8, Genre.ACTION: 0.8, Genre.ADVENTURE: 0.4}
    b = {Genre.WESTERN: 0.4, Genre.ACTION: 0.4, Genre.ADVENTURE: 0.2}
    assert normalize(a) == b
