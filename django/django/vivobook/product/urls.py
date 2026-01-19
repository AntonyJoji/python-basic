from django.urls import path
from .views import *
urlpatterns = [
    path('landingpage', landingpage),
    path('producthome', homepage),
]