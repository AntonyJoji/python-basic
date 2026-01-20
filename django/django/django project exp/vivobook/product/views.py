from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def landingpage(req):
    return render(req, 'landingpage.html')

def homepage(req):
    page = loader.get_template('homepage.html')
    data ={

        'catagory':'Appliances',
        'product':[
            {
                'name':'Washing Machine',
                'price':45000,
                'brand':'LG',
                'description':['Fully Automatic , Front Load, 6.5 Kg']
            },
            {
                'name':'Refrigerator',
                'price':55000,
                'brand':'Samsung',
                'description':['Double Door, Frost Free, 253 Ltrs']
            },
            {
                'name':'Air Conditioner',
                'price':60000,
                'brand':'Voltas',
                'description':['1.5 Ton, 5 Star, Inverter Split AC']
            },
            {
                'name':'Microwave Oven',
                'price':15000,
                'brand':'IFB',
                'description':['Convection,  Grill, 20 Ltrs']
            }
        ]
    }
    response = page.render(data, req)
    return HttpResponse(response)

def dbitemdisp(req):
    page = loader.get_template('dbitemdisp.html')
    data ={}
    response = page.render(data, req)
    return HttpResponse(response)