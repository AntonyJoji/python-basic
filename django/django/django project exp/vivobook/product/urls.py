
from django.urls import include, path
from .views import *
urlpatterns = [
    path('', landingpage),
    path('prohome/', homepage),
    path('dbitem/', dbitemdisp),
    path('details/<str:key>/', products),
    path('addtocart/', addtocart),
]