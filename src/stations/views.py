import folium
from django.shortcuts import render, get_object_or_404

from trains.models import *


def detail(request, slug):
    station = get_object_or_404(Station, slug=slug)
    m = folium.Map([station.__dict__.get('lat'), station.__dict__.get('lon')],
                   max_bounds=True,
                   min_lat=station.__dict__.get('lat') - 0.03, max_lat=station.__dict__.get('lat') + 0.03,
                   min_lon=station.__dict__.get('lon') - 0.03, max_lon=station.__dict__.get('lon') + 0.03,
                   zoom_start=17, max_zoom=18, min_zoom=13)  # updated
    m = m._repr_html_()
    context = {'my_map': m, 'object': station, 'weekday': ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"],
               'trains_list': Train.objects.all()}
    return render(request, 'stations/detail.html', context)


def stations_list(request):
    qs = Station.objects.all()
    context = {'objects_list': qs}
    return render(request, 'stations/list.html', context)
