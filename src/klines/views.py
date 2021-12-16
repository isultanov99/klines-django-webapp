from django.contrib import messages
from django.shortcuts import render
from stations.models import *
from trains.models import *
from django.shortcuts import redirect


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def check_input(get_request):
    from_input = str(get_request.get('from_field'))
    to_input = str(get_request.get('to_field'))
    if Station.objects.filter(name=from_input).exists() and Station.objects.filter(name=to_input).exists():
        return True
    else:
        return False


def home(request):
    if request.method == "POST" and check_input(request.POST):
        return redirect('route/' + Station.objects.get(name=str(request.POST.get('from_field'))).slug + '/' +
                        Station.objects.get(name=str(request.POST.get('to_field'))).slug)
    return render(request, 'home.html')


def route(request, first_param=None, second_param=None):
    context = {"first_param": Station.objects.get(slug=first_param),
               "second_param": Station.objects.get(slug=second_param),
               "trains": Train.objects.all(), "weekday": ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]}
    return render(request, 'route.html', context)
