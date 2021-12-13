from django.urls import path

from stations.views import *

urlpatterns = [
    path('', list, name='list'),
    path('<str:slug>/', detail, name='detail'),
]
