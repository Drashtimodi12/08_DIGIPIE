from django.contrib import admin
from django.urls import path
from myblog.views import *
# from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('', index, name='index'),
    path('post', PostAPI.as_view(), name='post'),
    path('post/<int:id>', PostAPIByID.as_view()),

    path('comment', CommentList, name='CommentList'),
    path('comment/<int:pid>', CommentAdd, name='CommentAdd'),
    path('comment/<int:id>', CommentAPIByID.as_view()),
    
    # path('api-token-auth/', views.obtain_auth_token)

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
