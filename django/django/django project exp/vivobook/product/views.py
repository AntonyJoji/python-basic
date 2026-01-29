from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import data
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
    db=data.objects.all()
    dataval ={'prods':db}
    response = page.render(dataval, req)
    return HttpResponse(response)

def products(req,key):
    page = loader.get_template('productdetails.html')
    db=data.objects.get(name=key)
    datas ={'pro':db}
    response = page.render(datas, req)
    return HttpResponse(response)

# def addtocart(req):
#     proid=req.GET['proid']
#     qty=req.GET['qty']
#     data=req.COOKIES.get('pid')
#     if data:
#         data=data+','+proid+":"+qty
#     else:
#         data=proid+":"+qty
    
#     response=render(req, 'cart.html', {'proid': proid, 'qty': qty})
#     response.set_cookie('pid', data)
#     return response

# def viewcart(req):
#     page = loader.get_template('shopingcart.html')
#     db=req.COOKIES.get('pid')
#     if db!=None:
#         items=db.split(',')
#         values={}
#         for i in items:
#             proid, qty = i.split(':')
#             values[proid]=qty
#         print(items)
#         response =page.render({'mycart':values},req)   
#     else:
#         response =page.render( {'Empty_cart':True},req)
#     return HttpResponse(response)


def addtocart(req):
    proid =req.GET['proid']
    qty =req.GET['qty']
    respone=render(req,'cart1.html')
    cartitems= {}
    if req.session.__contains__('cartdata'):
        cartitems=req.session['cartdata']
    cartitems[proid]=qty
    req.session['cartdata']=cartitems
    print(cartitems)
    print(req.session.get('cartdata'))
    return respone


def viewcart(req):
    page = loader.get_template('shopingcart1.html')
    if req.session.__contains__('cartdata'):
        for key in req.session.keys():
            if key =='cartdata':
               items=list(req.session[key].items())
               itemsdb=[]
               for i in items:
                   proid, qty = i
                   db=data.objects.get(id=proid)
                   itemsdb.append({
                                   'id':proid,
                                   'name':db.name,
                                   'price':db.price,
                                   'qty':qty,
                                   'desc':db.desc,
                                   'fea':db.fea,
                                   'total':db.price*int(qty),
                                   })
                   cart_sum=[i['total'] for i in itemsdb]
        response =page.render({'pros':itemsdb, 'cart_total':sum(cart_sum)},req)   
    else:
        response =page.render( {'Empty_cart':True},req)
    return HttpResponse(response)

from django.shortcuts import redirect

def clearcart(req):
    if 'cartdata' in req.session:
        del req.session['cartdata']
        return redirect('/dbitem')
    else:
        return HttpResponse("No items in cart to clear.")

