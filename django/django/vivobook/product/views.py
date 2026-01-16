from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def homepage(req):
    page =loader.get_template("producthome.html")
    data ={}
    response =page.render(data,req)
    return HttpResponse(response)

