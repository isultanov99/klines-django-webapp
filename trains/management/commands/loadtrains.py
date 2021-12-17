import csv
import json
from collections import OrderedDict

from django.core.management import BaseCommand
from trains.models import Train
from stations.models import *


class Command(BaseCommand):
    help = 'Load a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        i = 1
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                Train.objects.create(
                    num=row[0],
                    line=Line.objects.get(id=row[1]),
                    from_station=Station.objects.get(id=row[2]),
                    to_station=Station.objects.get(id=row[3]),
                    timetable=OrderedDict(json.loads(row[4])),
                    days=json.loads(row[5]),
                )
