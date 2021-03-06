from django.shortcuts import render, get_object_or_404
from trains.models import Train
from stations.models import Station


def trains_list(request):
    tl = Train.objects.all()
    sl = Station.objects.all()
    wd = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    context = {'trains_list': tl, 'stations_list': sl, 'weekday': wd}
    return render(request, '../templates/trains/list.html', context)


def detail(request, num):
    qs = get_object_or_404(Train, num=num)
    wd = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    context = {'object': qs, 'station': Station.objects.all(), 'weekday': wd}
    return render(request, '../templates/trains/detail.html', context)
