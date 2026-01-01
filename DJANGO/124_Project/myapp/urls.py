from django.urls import path    # Import path function to define URL patterns

from django.conf import settings    # Import settings to check DEBUG mode
from django.conf.urls.static import static  # Used to serve media files (images, files) during development


from rest_framework.authtoken import views      # Import DRF Token Authentication view (Token-based auth)

# Import JWT authentication views (access & refresh token)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,     # For generating access + refresh token
    TokenRefreshView         # For refreshing access token
)

from myapp.views import *      # Import all views from myapp.views



# URL patterns list

urlpatterns = [
    # path('', userprofile_page, name='userprofile_page'),























    # User APIs
    path('users/', get_users, name='get_users'),
    path('users/<int:id>/', get_usersbyId, name='get_usersbyId'),

    # UserProfile APIs
    path('getuserprofiles/', get_userprofile, name='get_userprofile'),
    path('postuserprofiles/user/<int:id>/', post_userprofile, name='post_userprofile'),
    path('userprofiles/<int:uid>/', UserProfileAPIByID.as_view()),

    # Category APIs
    path('categories/', CategoryAPI.as_view()),
    path('categories/<int:cid>/', CategoryAPIByID.as_view()),

    # Product APIs
    path('products/', get_products, name='get_products'),
    path('products/category/<int:cid>/', post_products, name='post_products'),
    path('products/<int:pid>/category/<int:cid>/', put_productByID, name='put_productByID'),
    path('products/<int:pid>/', ProductAPIByID.as_view()),


    # Order APIs
    path('orders/', get_orders, name='get_orders'),
    path('orders/product/<int:pid>/user/<int:id>/', post_orders, name='post_orders'),
    path('orders/<int:oid>/product/<int:pid>/user/<int:id>/', put_orderByID, name='put_orderByID'),
    path('orders/<int:oid>/', OrderDetailAPI.as_view()),


    # ==============================
    # DRF Token Authentication URL
    # ==============================
    # Generates a token using username & password
    # Used in TokenAuthentication
    path('api-token-auth/', views.obtain_auth_token),

    # ==============================
    # JWT Authentication URLs
    # ==============================
    # Generates Access Token + Refresh Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Generates new Access Token using Refresh Token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# ==============================
# Media File Configuration
# ==============================
# This allows serving media files (like images) during development only
# Example: ImageField, FileField
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
