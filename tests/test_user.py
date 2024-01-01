from movie_data_generator.user import User
from movie_data_generator.genre import Genre


def test_instantiate_user():
    profile = {Genre.WESTERN: 0.8, Genre.ACTION: 0.8, Genre.ADVENTURE: 0.4}
    User(coverage=0.8, profile=profile)
