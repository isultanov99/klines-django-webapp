from collections import OrderedDict
from django.db import models
from stations.models import *


class Train(models.Model):
    num = models.SmallIntegerField(primary_key=True)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    from_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='from_set')
    to_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='to_set')
    timetable = models.JSONField(default=dict)
    days = models.JSONField(default=list)

    class Meta:
        ordering = ['line', 'from_station', 'num']
