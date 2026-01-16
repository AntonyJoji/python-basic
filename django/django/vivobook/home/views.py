from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homecall(req):
    return HttpResponse("<h1>This is Home Page hello antony</h1>")


def home(req):
    return render(req,'home.html')


def addval(req):
    val1 = int(req.POST['first_value'])
    val2 = int(req.POST['second_value'])
    res = val1 + val2
    return render(req, 'result.html', {'result': res})
    