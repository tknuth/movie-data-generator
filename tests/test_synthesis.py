# import random

# from movie_data_generator.movie import load_movies
# from movie_data_generator.profile import load_profiles
# from movie_data_generator.synthesis import sample, similarity, create_random_user


# def test_sample():
#     random.seed(1)
#     l = [1, 2, 3, 4, 5]
#     assert sample(l, 0.5) == [3, 4]
#     assert sample(l, 0.6) == [1, 3, 2]
#     assert l == [1, 2, 3, 4, 5]


# def test_create_random_user():
#     random.seed(1)

#     profiles = load_profiles()
#     movies = load_movies()

#     a = create_random_user(profiles)
#     b = create_random_user(profiles)

#     print()
#     print(a.profile, movies[0].profile)
#     print()
#     print(movies[0].slug)
#     print(similarity(a.profile, movies[0].profile))
