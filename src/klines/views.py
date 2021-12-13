from django.shortcuts import render, get_object_or_404

from stations.models import Station


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def home(request):
    # if request.method == 'POST':

    return render(request, 'home.html')


def match(request, first_param=None, second_param=None):
    context = {"first_param": first_param, "second_param": second_param}
    return render(request, 'route.html', context)
