from django.urls import path
from crudapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_data', add_data, name="add_data"),
    path('loaddata', loaddata, name="loaddata"),
    path('deletedata', deletedata, name="deletedata"),
    path('databyid', databyid, name="databyid"),
    path('updatedata', updatedata, name="updatedata"),
    path('searchdata', searchdata, name="searchdata")
]
