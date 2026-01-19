from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homecall (req):
    return HttpResponse("<h1>antony joji</h1>")

def home(req):
    return render (req,'home.html')

def addval (req):
    val1=int (req.POST['num1'])
    val2=int (req.POST['num2'])
    res=val1+val2
    return render (req,'result.html',{'result':res})