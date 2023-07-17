import pytest
from comparisons.comparisons import sort_movies_by_title, sort_movies_by_year
from comparisons.movies import Movie

# Test cases for sorting movies

def test_sort_movies_by_year():
    movies = [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Annie", 1982, ["Comedy", "Drama", "Family"]),
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
        Movie("The Lion King", 1994, ["Animation", "Adventure", "Drama"]),
        Movie("The Shawshank Redemption", 1994, ["Drama"]),
        Movie("Avatar", 2009, ["Action", "Adventure", "Fantasy"]),
    ]

    sorted_movies = sort_movies_by_year(movies)
    assert sorted_movies[0].title == "The Avengers"
    assert sorted_movies[0].year == 2012
    assert sorted_movies[-1].title == "Annie"
    assert sorted_movies[-1].year == 1982


def test_sort_movies_by_title():
    movies = [
        Movie("The Avengers", 2012, ["Action", "Adventure", "Sci-Fi"]),
        Movie("Annie", 1982, ["Comedy", "Drama", "Family"]),
        Movie("A Beautiful Mind", 2001, ["Biography", "Drama"]),
        Movie("The Lion King", 1994, ["Animation", "Adventure", "Drama"]),
        Movie("The Shawshank Redemption", 1994, ["Drama"]),
        Movie("Avatar", 2009, ["Action", "Adventure", "Fantasy"]),
    ]

    sorted_movies = sort_movies_by_title(movies)
    sorted_titles = [movie.title for movie in sorted_movies]
    print(sorted_titles)
    assert sorted_movies[0].title == "Annie"
    assert sorted_movies[-1].title == "The Shawshank Redemption"