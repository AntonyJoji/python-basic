from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def landingpage(req):
    return render(req, "landingpage.html")


def homepage(req):
    page =loader.get_template("homepage.html")
    data ={
        'category':'Appliances',
        'products':[
            {
                'id':101,
                'item':'Washing Machine',
                'price':45000,
                'brand':'LG',
                'description':['High efficiency front load washing machine']
            },
             {
                'id':102,
                'item':'Microwave Oven',
                'price':25000,
                'brand':'Samsung',
                'description':['Convection microwave oven with grill', '800W power']
            },
                {
                    'id':103,
                    'item':'Refrigerator',
                    'price':55000,
                    'brand':'Whirlpool',
                    'description':['Double door refrigerator with freezer', 'Frost free']
                },
                {
                'id':104,
                'item':'T.V',
                'price':44000,
                'brand':'Samsung',
                'description': ['42 inch smart LED T.V', '4K Ultra HD']
            }
        ]
    }
    response =page.render(data,req)
    return HttpResponse(response)

