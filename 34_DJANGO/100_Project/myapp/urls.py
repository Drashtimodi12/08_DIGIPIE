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
