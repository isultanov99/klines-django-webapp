import csv


from django.core.management import BaseCommand
from stations.models import Station
from slugify import slugify


class Command(BaseCommand):
    help = 'Load a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        i = 1
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                Station.objects.create(
                    id=i,
                    name=row[0],
                    lat=row[1],
                    lon=row[2],
                    slug=slugify(row[0])
                )
                i += 1
