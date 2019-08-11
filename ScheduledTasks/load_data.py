from imdb import data
from Movies.models import MovieDetails
from Utility.retry_decorator import retry


@retry(Exception)
def load_movie_details():
    print("Starting initial load.")
    for d in data:
        try:
            MovieDetails.objects.get(name=d['name'])
        except Exception as ex:
            movie = MovieDetails()
            movie.popularity = d['99popularity']
            movie.director = d['director']
            movie.genre = d['genre']
            movie.imdb_score = d['imdb_score']
            movie.name = d['name']
            movie.save()
    print("Completed initial load.")
