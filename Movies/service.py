from .models import MovieDetails


def search_by(key, value):
    if key == 'genre':
        movie_details = MovieDetails.objects.filter(**{key + '__contains': [value]})
    else:
        movie_details = MovieDetails.objects.filter(**{key: value})
        if not movie_details and key in ['name', 'director']:
            movie_details = MovieDetails.objects.filter(**{key + '__contains': value})
    return movie_details
