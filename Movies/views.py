from .service import search_by
from .models import MovieDetails
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@csrf_exempt
def show(request):
    """Endpoint for movie details and search"""
    key, value = request.POST.get("search_by", request.GET.get("search_by", None)), \
                 request.POST.get("search_text", request.GET.get("search_text", None))
    if key and value:
        movie_details = search_by(key, value)
    else:
        movie_details = MovieDetails.objects.all()
    return pagination_handler(request, movie_details, key, value)


def pagination_handler(request, movie_details, key, value):
    """Method for handling Pagination using Django Paginator"""
    page = request.GET.get('page', 1)
    paginator = Paginator(movie_details, 25)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)
    return render(request, "movie_details.html", {'movies': movies, 'search_by': key, 'search_text': value})
