from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def search(request):
    data = request.GET['data']
    # print(data)
    rows = ""
    if data == 'sports':
        rows += """<ul>
        <li>BAT</li>
        <li>BAll</li>
        <li>VollyBall</li>
        <li>Racet</li>
        <li>Gloves</li>
        </ul>"""
    elif data == "electric":
        rows += """<ul>
        <li>TV</li>
        <li>Lights</li>
        <li>Laptop</li>
        <li>Fridge</li>
        <li>AC</li>
        </ul>"""
    return HttpResponse(rows)


def filter(request):
    data = request.GET['data']
    # products = Product.objects.all()

    products = Product.objects.filter(name__startswith=data)
    return JsonResponse({"data":list(products.values())})

def countries(request):
    allcontries = Country.objects.all()
    return JsonResponse({"data":list(allcontries.values())})

def states(request):
    cid = request.GET['cid']
    allstates = State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(allstates.values())})

def cities(request):
    sid = request.GET['sid']
    allcitiies = City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(allcitiies.values())})
