
from django.urls import path
from .views import *
urlpatterns = [
    path('h', homecall),
    path("c", call)
]
