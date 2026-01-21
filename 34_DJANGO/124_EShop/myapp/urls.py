from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *


urlpatterns = [
    path('', index, name='index'),
    path('accounts', accounts, name='accounts'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('details', details, name='details'),
    path('login_register', login_register, name='login_register'),
    path('shop', shop, name='shop'),

    path('register_user', register_user, name='register_user'),
    path('login_user', login_user, name='login_user'),
    path('logout_user', logout_user, name='logout_user'),

    path('categories', categories, name='categories'),
    path('products', products, name='products'),

    path("addtocart",addtocart,name="addtocart"),
    path("deletecart",deletecart,name="deletecart"),
    path("changeqty",changeqty,name="changeqty"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)