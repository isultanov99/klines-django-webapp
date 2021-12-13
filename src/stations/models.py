from django.db import models
from slugify import slugify


class Station(models.Model):
    name = models.CharField(max_length=50, verbose_name='Station name', unique=True, primary_key=True)
    lat = models.FloatField(verbose_name='Latitude (dec degrees)')
    lon = models.FloatField(verbose_name='Longitude (dec degrees)')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name
