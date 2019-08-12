from .models import MovieDetails


def search_by(key, value):
    """Handling for different types of searches. Includes fallback logic as well."""
    if key == 'genre':
        movie_details = MovieDetails.objects.filter(**{key + '__contains': [value]})
    else:
        if key in ['popularity', 'imdb_score']:
            value = safe_cast(value)
        elif key in ['popularity__lte', 'popularity__gte', 'imdb_score__lte', 'imdb_score__gte']:
            value = safe_cast(value, 0.0)
        movie_details = MovieDetails.objects.filter(**{key: value})
        if not movie_details and key in ['name', 'director']:
            movie_details = MovieDetails.objects.filter(**{key + '__contains': value})
    return movie_details


def safe_cast(val, default=None):
    """Safe type casting of numbers"""
    try:
        return round(float(val), 1)
    except (ValueError, TypeError):
        return default
