from django.urls import path
from API_App.views import *

urlpatterns = [
    # ------------------------
    # Student
    # ------------------------

    path("getStudents", view, name="view"),
    path('addStudents', add, name='add'),
    path('updateStudent/<int:id>', update, name='update'),
    path('deleteStudent/<int:id>', delete, name='delete'),


    # ------------------------
    # Employee
    # ------------------------
    path("employee", view_emp, name='view_emp'),
    path("employee/", add_emp, name='add_emp'),
    path("employee/<int:id>", update_emp, name='update_emp'),
    path("employee/<int:id>/", delete_emp, name='delete_emp'),

    # ------------------------
    # Products
    # ------------------------
    path('products', ProductAPI.as_view()),
]
