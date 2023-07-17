

def sort_movies_by_title(movies):
    def remove_prefix(title):
        prefixes = ["A ", "An ", "The "]
        for prefix in prefixes:
            if title.startswith(prefix):
                return title[len(prefix):].strip()
        return title

    return sorted(movies, key=lambda movie: remove_prefix(movie.title).lower())


def sort_movies_by_year(movies):
    return sorted(movies, key=lambda movie: movie.year, reverse=True)
