from django.urls import path

from trains.views import *

urlpatterns = [
    path('', trains_list, name='list'),
    path('<int:num>/', detail, name='detail'),
]
