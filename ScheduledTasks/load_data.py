from imdb import data
from Movies.models import MovieDetails
from Utility.retry_decorator import retry
# from Utility.trie_autocomplete import add_word


@retry(Exception)
def load_movie_details():
    """Method for initial load of data dump provided"""
    print("Starting initial load.")
    for d in data:
        try:
            MovieDetails.objects.get(name=d['name'])
            # add_word(d['name']) TODO
        except Exception:
            movie = MovieDetails()
            movie.popularity = d['99popularity']
            movie.director = d['director']
            movie.genre = d['genre']
            movie.imdb_score = d['imdb_score']
            movie.name = d['name']
            movie.save()
    print("Completed initial load.")
