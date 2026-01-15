from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from API_Company.views import *

urlpatterns = [
    # ---------- Department URLs ----------
    path('department', departmentAPI.as_view()),
    path('department/<int:id>', departmentAPIByID.as_view()),

    # ---------- Employee URLs ----------
    path('employee', employeeview, name='employeeview'),
    path('employee/departmetnt/<int:did>', employeeadd, name='employeeadd'),
    path('employee/<int:id>/departmetnt/<int:did>', employeeupdate, name='employeeupdate'),
    path('employee/<int:id>', EmployeeAPIByID.as_view()),

    # ---------- djangorestframework Auth URLs ----------
    path('api-token-auth/', views.obtain_auth_token),

    
    # ---------- djangorestframework-simplejwt Auth URLs ----------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
