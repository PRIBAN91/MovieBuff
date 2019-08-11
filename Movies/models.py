from django.db import models
from Utility.constants import ADMIN
from django.contrib.postgres.fields import ArrayField


class MovieDetails(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    created_by = models.CharField(blank=False, max_length=255, default=ADMIN)
    last_updated_at = models.DateTimeField(auto_now=True, blank=False)
    last_updated_by = models.CharField(blank=False, max_length=255, default=ADMIN)
    name = models.CharField(max_length=255, db_index=True)
    popularity = models.DecimalField(max_digits=10, null=True, decimal_places=1)
    director = models.CharField(max_length=100, db_index=True)
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1)
    genre = ArrayField(models.CharField(max_length=100), null=True)

    class Meta:
        db_table = "movie_details"
        unique_together = ['id', 'name']
        ordering = ['id', ]
        managed = True
