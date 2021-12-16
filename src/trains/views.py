from django.shortcuts import render, get_object_or_404
from trains.models import Train
from stations.models import Station


def trains_list(request):
    tl = Train.objects.all()
    sl = Station.objects.all()
    wd = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    context = {'trains_list': tl, 'stations_list': sl, 'weekday': wd}
    return render(request, 'trains/list.html', context)


def detail(request, num):
    qs = get_object_or_404(Train, num=num)
    wd = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    context = {'object': qs, 'station': Station.objects.all(), 'weekday': wd}
    return render(request, 'trains/detail.html', context)
