from django.db import models


class Line(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Station name')
    lat = models.FloatField(verbose_name='Latitude (dec degrees)')
    lon = models.FloatField(verbose_name='Longitude (dec degrees)')
    slug = models.SlugField()
    line = models.ManyToManyField(Line)

    def __str__(self):
        return self.name


