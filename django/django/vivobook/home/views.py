from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homecall(req):
    return HttpResponse("This is Home Page hello antony")


def call (req):
    return HttpResponse("<h1>This is Call Page</h1>")