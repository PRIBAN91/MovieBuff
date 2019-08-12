from django.contrib import admin
from Movies.models import MovieDetails

admin.site.register(MovieDetails)  # MovieDetails model registered for CRUD operations through Django admin panel
