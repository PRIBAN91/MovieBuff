from .models import MovieDetails
from rest_framework import serializers


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDetails
        exclude = ('created_at', 'created_by', 'last_updated_at', 'last_updated_by')
