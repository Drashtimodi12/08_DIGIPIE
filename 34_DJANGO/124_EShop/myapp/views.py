from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from myapp.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def accounts(request):
    return render(request, 'accounts.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def details(request):
    return render(request, 'details.html')

def login_register(request):
    return render(request, 'login-register.html')

def shop(request):
    return render(request, 'shop.html')

def register_user(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")

            if not username or not email or not password:
                return render(request, 'login-register.html', {'msg': 'All fields are rquired...'})
            else:
                if User.objects.filter(username=username).exists():
                    return render(request, 'login-register.html', {'msg': 'Username already exists!'})
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return render(request, "login-register.html", {'msg': 'Registration successful! Please log in.'})
        return render(request, 'login-register.html')
    except Exception as e:
        return render(request, 'login-register.html', {'errors': str(e), 'message': 'Something wents wrong!'}) 


def login_user(request):
    try:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            if not username or not password:
                return render(request, 'login-register.html', {'msg': 'Username and password are required!'})
            else:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, 'login-register.html', {'msg': 'Invalid username or password!'}) 
        return render(request, 'login_user.html')
    except Exception as e:
        return render(request, 'login-register.html', {'errors': str(e), 'message': 'Something wents wrong!'}) 


def logout_user(request):
    logout(request)
    return render(request, "login-register.html", {"msg": "You have been logged out successfully."})


def categories(request):
    categories = Category.objects.all()
    return JsonResponse({'categories': list(categories.values())})

        
def products(request):
    products = Product.objects.all()
    data = []
    for p in products:
        data.append({
            "id": p.id,
            "name": p.name,
            "price": float(p.price),
            "image1": p.image1.url,
            "image2": p.image2.url,
            "category": p.category.name
        })
    return JsonResponse({'products': data})

def addtocart(request):
    try :
        pid = request.GET['pid']
        user = request.user
    

        if user.is_anonymous:
            return HttpResponse(user)
        else :                 
            product = Product.objects.get(pk=pid)
            isExist =   Cart.objects.filter(user=user,product=product).exists()
            if not isExist:
                cart =  Cart.objects.create(user=user,product=product)
                if cart:
                    return HttpResponse("Product added into the cart !")
            else:
                return HttpResponse("Product already exist !!!")
    except Exception as e :
        print(e)

def deletecart(request):
    cid = request.GET['cid']
    cart = Cart.objects.get(pk=cid)
    cart.delete()
    return HttpResponse("Item removed from cart")

def changeqty(request):
    qty = request.GET['qty']
    cid = request.GET['cid']

    cart = Cart.objects.get(pk=cid)
    cart.quantity=qty
    cart.save()
    return HttpResponse("Qty changed...")