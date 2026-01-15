# Importing 'render' to display HTML templates, 'redirect' to send the user to a different URL
from django.shortcuts import render, redirect  

# Importing 'HttpResponse' to send plain text or custom responses to the browser
from django.http import HttpResponse  

# Importing all models from 'myapp' so we can access the database tables
from myapp.models import *  

# Importing 'JsonResponse' to send JSON data, commonly used in API responses
from django.http import JsonResponse 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    data = request.GET['data']
    # print(data)
    # rows = ""
    # if data == 'sports':
    #     rows+="<ul><li>Football</li><li>Cricket</li><li>Basketball</li></ul>"
    # elif data == 'electronics':
    #     rows+="<ul><li>Mobile</li><li>TV</li><li>Laptop</li></ul>"
    # return HttpResponse(rows)


    # products = Product.objects.all()
    products = Product.objects.filter(name__startswith=data)
    return JsonResponse({"data":list(products.values())})
    

def countries(rquest):
    allcountries = Country.objects.all()
    return JsonResponse({"data":list(allcountries.values())})


def states(request):
    cid = request.GET['cid']
    allstates = State.objects.filter(country_id=cid)
    return JsonResponse({"data": list(allstates.values())})

def cities(request):
    sid = request.GET['sid']
    allcities = City.objects.filter(state_id=sid)
    return JsonResponse({"data": list(allcities.values())})


