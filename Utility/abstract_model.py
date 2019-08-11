from django.db import models
from Utility.constants import ADMIN


class Base(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    created_by = models.CharField(blank=False, max_length=255, default=ADMIN)
    last_updated_at = models.DateTimeField(auto_now=True, blank=False)
    last_updated_by = models.CharField(blank=False, max_length=255, default=ADMIN)
